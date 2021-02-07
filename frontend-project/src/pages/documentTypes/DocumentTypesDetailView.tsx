import { PageHeaderWrapper } from '@ant-design/pro-layout';
import { Button, Col, Card, Form, Input, Row, Space, Spin } from 'antd';
import { connect, useDispatch } from 'dva';
import React, { useEffect, useState } from 'react';
import { formatMessage, FormattedMessage } from 'umi-plugin-react/locale';
import { DocumentType } from '@/services/definitions';
import { ReduxResourceState } from '@/utils/reduxModel';
import router from 'umi/router';
import { RouterTypes } from 'umi';
import { ServiceResponse } from '@/services/service';
import { openNotificationWithIcon } from '@/models/global';
import { localeKeys } from '../../locales/pl-PL';

interface DocumentTypesDetailViewProps {
  documentTypes: ReduxResourceState<DocumentType>;
  match: RouterTypes['match'] & { params: { id: string | undefined } };
}

const layout = {
  labelCol: { span: 8 },
  wrapperCol: { span: 16 },
};

const tailLayout = {
  wrapperCol: { offset: 8, span: 16 },
};

function DocumentTypesDetailView({ documentTypes, match }: DocumentTypesDetailViewProps) {
  const dispatch = useDispatch();
  const isEdit = Boolean(match.params.id);
  const editetDocumentTypes = documentTypes.data.find(
    value => value.id === Number(match.params.id),
  );
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [form] = Form.useForm();
  function onRequestDone(response: ServiceResponse<DocumentType>) {
    setIsSubmitting(false);
    if (response.status === 'success') {
      router.push('/documentTypes');
    } else if (response.statusCode === 400) {
      form.setFields(
        Array.from(
          Object.entries(response.errorBody),
        ).map(([name, errors]: [string, Array<string>]) => ({ name, errors })),
      );
    } else {
      openNotificationWithIcon(
        'error',
        formatMessage({ id: localeKeys.error }),
        `${formatMessage({
          id: isEdit
            ? localeKeys.documentTypes.detailView.errors.updateFailed
            : localeKeys.documentTypes.detailView.errors.createFailed,
        })} ${response.errorText}`,
      );
    }
  }

  function onFinish() {
    if (isEdit) {
      dispatch({
        type: 'documentTypes/update',
        payload: {
          ...form.getFieldsValue(),
          id: match.params.id,
          onResponse: onRequestDone,
        },
      });
    } else {
      dispatch({
        type: 'documentTypes/create',
        payload: {
          ...form.getFieldsValue(),
          onResponse: onRequestDone,
        },
      });
    }
    setIsSubmitting(true);
  }

  useEffect(() => {
    if (isEdit)
      dispatch({ type: 'documentTypes/fetchOne', payload: { id: Number(match.params.id) } });
  }, []);

  if (documentTypes.isLoading || (isEdit && !editetDocumentTypes) || isSubmitting) {
    return (
      <Row justify="center">
        <Col>
          <Spin size="large" />
        </Col>
      </Row>
    );
  }
  if (isEdit) form.setFieldsValue(editetDocumentTypes);

  return (
    <Form {...layout} form={form} onFinish={onFinish}>
      <PageHeaderWrapper
        content={formatMessage({
          id: isEdit
            ? localeKeys.documentTypes.detailView.editPageHeaderContent
            : localeKeys.documentTypes.detailView.newPageHeaderContent,
        })}
      >
        <Card bordered={false}>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: localeKeys.documentTypes.fields.name })}
                name="name"
                rules={[
                  {
                    required: true,
                    message: formatMessage({ id: localeKeys.documentTypes.detailView.errors.name }),
                  },
                ]}
              >
                <Input
                  placeholder={formatMessage({
                    id: localeKeys.documentTypes.detailView.placeholders.name,
                  })}
                />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item {...tailLayout}>
                <Space>
                  <Button type="primary" htmlType="submit">
                    <FormattedMessage id={localeKeys.form.save} />
                  </Button>
                </Space>
              </Form.Item>
            </Col>
          </Row>
        </Card>
      </PageHeaderWrapper>
    </Form>
  );
}

export default connect((props: DocumentTypesDetailViewProps) => props)(DocumentTypesDetailView);
