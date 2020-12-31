import { PageHeaderWrapper } from '@ant-design/pro-layout';
import { Button, Col, Card, Form, Input, Row, Space, Spin } from 'antd';
import { connect, useDispatch } from 'dva';
import React, { useEffect, useState } from 'react';
import { formatMessage, FormattedMessage } from 'umi-plugin-react/locale';
import { Tag } from '@/services/definitions';
import { ReduxResourceState } from '@/utils/reduxModel';
import router from 'umi/router';
import { RouterTypes } from 'umi';
import { ServiceResponse } from '@/services/service';
import smallEodSDK from '@/utils/sdk';
import { openNotificationWithIcon } from '@/models/global';
import { localeKeys } from '../../locales/pl-PL';

interface TagsDetailViewProps {
  tags: ReduxResourceState<Tag>;
  match: RouterTypes['match'] & { params: { id: string | undefined } };
}

const layout = {
  labelCol: { span: 8 },
  wrapperCol: { span: 16 },
};

const tailLayout = {
  wrapperCol: { offset: 8, span: 16 },
};

function TagsDetailView({ tags, match }: TagsDetailViewProps) {
  const dispatch = useDispatch();
  const isEdit = Boolean(match.params.id);
  const editetTags = tags.data.find(value => value.id === Number(match.params.id));
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [form] = Form.useForm();
  (window as any).se = smallEodSDK;
  function onRequestDone(response: ServiceResponse<Tag>) {
    setIsSubmitting(false);
    if (response.status === 'success') {
      router.push('/tags/list');
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
            ? localeKeys.tags.detailView.errors.updateFailed
            : localeKeys.tags.detailView.errors.createFailed,
        })} ${response.errorText}`,
      );
    }
  }

  function onFinish() {
    if (isEdit) {
      dispatch({
        type: 'tags/update',
        payload: {
          ...form.getFieldsValue(),
          id: match.params.id,
          onResponse: onRequestDone,
        },
      });
    } else {
      dispatch({
        type: 'tags/create',
        payload: {
          ...form.getFieldsValue(),
          onResponse: onRequestDone,
        },
      });
    }
    setIsSubmitting(true);
  }

  useEffect(() => {
    if (isEdit) dispatch({ type: 'tags/fetchOne', payload: { id: Number(match.params.id) } });
  }, []);

  if (tags.isLoading || (isEdit && !editetTags) || isSubmitting) {
    return (
      <Row justify="center">
        <Col>
          <Spin size="large" />
        </Col>
      </Row>
    );
  }
  if (isEdit) form.setFieldsValue(editetTags);

  return (
    <Form {...layout} form={form} onFinish={onFinish}>
      <PageHeaderWrapper
        content={formatMessage({
          id: isEdit
            ? localeKeys.tags.detailView.editPageHeaderContent
            : localeKeys.tags.detailView.newPageHeaderContent,
        })}
      >
        <Card bordered={false}>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: localeKeys.tags.fields.name })}
                name="name"
                rules={[
                  {
                    required: true,
                    message: formatMessage({ id: localeKeys.tags.detailView.errors.name }),
                  },
                ]}
              >
                <Input
                  placeholder={formatMessage({ id: localeKeys.tags.detailView.placeholders.name })}
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

export default connect((props: TagsDetailViewProps) => props)(TagsDetailView);
