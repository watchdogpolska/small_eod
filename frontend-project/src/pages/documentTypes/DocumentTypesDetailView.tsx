import { PageHeaderWrapper } from '@ant-design/pro-layout';
import { Button, Col, Card, Form, Input, Row, Space, Spin } from 'antd';
import React, { useEffect, useState } from 'react';
import { formatMessage, FormattedMessage } from 'umi-plugin-react/locale';
import router from 'umi/router';
import { localeKeys } from '../../locales/pl-PL';

import { getFormErrorFromPromiseError } from '@/utils/getFormErrorFromPromiseError';
import { DetailMatchParam } from '@/models/connect';
import { DocumentTypesService } from '@/services/documentTypes';
import { DocumentType } from '@/services/definitions';

const layout = {
  labelCol: { span: 8 },
  wrapperCol: { span: 16 },
};

const tailLayout = {
  wrapperCol: { offset: 8, span: 16 },
};

export default function DocumentTypesDetailView({ match }: DetailMatchParam) {
  const isEdit = Boolean(match.params.id);
  const [editedItem, setEditedItem] = useState<DocumentType | undefined>();
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [form] = Form.useForm();
  const {
    fields,
    detailView: { editPageHeaderContent, newPageHeaderContent, placeholders, errors },
  } = localeKeys.documentTypes;

  useEffect(() => {
    if (isEdit)
      DocumentTypesService.fetchOne(Number(match.params.id)).then(response =>
        setEditedItem(response),
      );
  }, []);

  function onError(response: any) {
    setIsSubmitting(false);
    if (response?.statusCode === 400) {
      form.setFields(getFormErrorFromPromiseError(response));
    }
  }

  function onSubmit() {
    const action = isEdit ? DocumentTypesService.update : DocumentTypesService.create;
    action({
      ...(form.getFieldsValue() as DocumentType),
      id: Number(match.params.id),
    })
      .then(() => {
        router.push('/documentTypes');
      })
      .catch(onError);
    setIsSubmitting(true);
  }

  if ((isEdit && !editedItem) || isSubmitting) {
    return (
      <Row justify="center">
        <Col>
          <Spin size="large" />
        </Col>
      </Row>
    );
  }
  if (isEdit) form.setFieldsValue(editedItem);

  return (
    <Form {...layout} form={form} onFinish={onSubmit}>
      <PageHeaderWrapper
        content={formatMessage({
          id: isEdit ? editPageHeaderContent : newPageHeaderContent,
        })}
      >
        <Card bordered={false}>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: fields.name })}
                name="name"
                rules={[
                  {
                    required: true,
                    message: formatMessage({ id: errors.name }),
                  },
                ]}
              >
                <Input
                  placeholder={formatMessage({
                    id: placeholders.name,
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
