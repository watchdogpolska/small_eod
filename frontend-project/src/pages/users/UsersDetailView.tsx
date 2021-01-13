import { PageHeaderWrapper } from '@ant-design/pro-layout';
import { Button, Col, Card, Form, Input, Row, Space, Spin } from 'antd';
import { connect, useDispatch } from 'dva';
import React, { useEffect, useState } from 'react';
import { formatMessage, FormattedMessage } from 'umi-plugin-react/locale';
import { User } from '@/services/definitions';
import { ReduxResourceState } from '@/utils/reduxModel';
import router from 'umi/router';
import { RouterTypes } from 'umi';
import { ServiceResponse } from '@/services/service';
import { openNotificationWithIcon } from '@/models/global';
import { localeKeys } from '../../locales/pl-PL';

interface UsersDetailViewProps {
  users: ReduxResourceState<User>;
  match: RouterTypes['match'] & { params: { id: string | undefined } };
}

const layout = {
  labelCol: { span: 8 },
  wrapperCol: { span: 16 },
};

const tailLayout = {
  wrapperCol: { offset: 8, span: 16 },
};

function UsersDetailView({ users, match }: UsersDetailViewProps) {
  const dispatch = useDispatch();
  const isEdit = Boolean(match.params.id);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const editedUser = users.data.find(value => value.id === Number(match.params.id));
  const [form] = Form.useForm();

  function onRequestDone(response: ServiceResponse<User>) {
    setIsSubmitting(false);
    if (response.status === 'success') {
      router.push('/users');
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
            ? localeKeys.users.detailView.errors.updateFailed
            : localeKeys.users.detailView.errors.createFailed,
        })} ${response.errorText}`,
      );
    }
  }

  function onFinish() {
    if (isEdit) {
      dispatch({
        type: 'users/update',
        payload: {
          ...form.getFieldsValue(),
          id: match.params.id,
          onResponse: onRequestDone,
        },
      });
    } else {
      dispatch({
        type: 'users/create',
        payload: {
          ...form.getFieldsValue(),
          onResponse: onRequestDone,
        },
      });
    }
    setIsSubmitting(true);
  }

  useEffect(() => {
    if (isEdit) dispatch({ type: 'users/fetchOne', payload: { id: Number(match.params.id) } });
  }, []);

  if (users.isLoading || (isEdit && !editedUser) || isSubmitting) {
    return (
      <Row justify="center">
        <Col>
          <Spin size="large" />
        </Col>
      </Row>
    );
  }
  if (isEdit) form.setFieldsValue(editedUser);

  return (
    <Form {...layout} form={form} onFinish={onFinish}>
      <PageHeaderWrapper
        content={formatMessage({
          id: isEdit
            ? localeKeys.users.detailView.editPageHeaderContent
            : localeKeys.users.detailView.newPageHeaderContent,
        })}
      >
        <Card bordered={false}>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: localeKeys.users.fields.username })}
                name="username"
                rules={[
                  {
                    required: true,
                    message: formatMessage({ id: localeKeys.users.detailView.errors.username }),
                  },
                ]}
              >
                <Input
                  placeholder={formatMessage({
                    id: localeKeys.users.detailView.placeholders.username,
                  })}
                />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: localeKeys.users.fields.password })}
                name="password"
                rules={[
                  {
                    required: true,
                    message: formatMessage({
                      id: localeKeys.users.detailView.errors.password,
                    }),
                  },
                ]}
              >
                <Input
                  type="password"
                  placeholder={formatMessage({
                    id: localeKeys.users.detailView.placeholders.password,
                  })}
                />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: localeKeys.users.fields.email })}
                name="email"
                rules={[
                  {
                    required: true,
                    message: formatMessage({ id: localeKeys.users.detailView.errors.email }),
                  },
                ]}
              >
                <Input
                  type="email"
                  placeholder={formatMessage({
                    id: localeKeys.users.detailView.placeholders.email,
                  })}
                />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: localeKeys.users.fields.firstName })}
                name="firstName"
              >
                <Input
                  placeholder={formatMessage({
                    id: localeKeys.users.detailView.placeholders.firstName,
                  })}
                />
              </Form.Item>
            </Col>
          </Row>

          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: localeKeys.users.fields.lastName })}
                name="lastName"
              >
                <Input
                  placeholder={formatMessage({
                    id: localeKeys.users.detailView.placeholders.lastName,
                  })}
                />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item {...tailLayout}>
                <Space>
                  <Button type="default" htmlType="reset">
                    <FormattedMessage id={localeKeys.form.reset} />
                  </Button>
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

export default connect((props: UsersDetailViewProps) => props)(UsersDetailView);
