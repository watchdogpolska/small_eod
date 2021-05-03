import { PageHeaderWrapper } from '@ant-design/pro-layout';
import { Button, Card, Col, Form, Input, Row, Spin } from 'antd';
import React, { useEffect, useState } from 'react';
import { formatMessage, FormattedMessage } from 'umi-plugin-react/locale';
import router from 'umi/router';
import { localeKeys } from '../../locales/pl-PL';
import { DetailMatchParam } from '../../models/connect';
import { User } from '../../services/definitions';
import { UsersService } from '../../services/users';
import { getFormErrorFromPromiseError } from '../../utils/getFormErrorFromPromiseError';

const layout = {
  labelCol: { span: 8 },
  wrapperCol: { span: 16 },
};

const tailLayout = {
  wrapperCol: { offset: 8, span: 16 },
};

export default function UsersDetailView({ match }: DetailMatchParam) {
  const isEdit = Boolean(match.params.id);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [editedItem, setEditedItem] = useState<User | undefined>();
  const [form] = Form.useForm();
  const {
    fields,
    detailView: { errors, placeholders, editPageHeaderContent, newPageHeaderContent },
  } = localeKeys.users;

  useEffect(() => {
    if (isEdit)
      UsersService.fetchOne(Number(match.params.id)).then(response => setEditedItem(response));
  }, []);

  function onError(response: any) {
    setIsSubmitting(false);
    if (response?.status === 400) {
      form.setFields(getFormErrorFromPromiseError(response));
    }
  }

  function onSubmit() {
    const action = isEdit ? UsersService.update : UsersService.create;
    action({
      ...(form.getFieldsValue() as User),
      id: Number(match.params.id),
    })
      .then(() => {
        router.push('/users');
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
                label={formatMessage({ id: fields.username })}
                name="username"
                rules={[
                  {
                    required: true,
                    message: formatMessage({ id: errors.username }),
                  },
                ]}
              >
                <Input
                  placeholder={formatMessage({
                    id: placeholders.username,
                  })}
                />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: fields.password })}
                name="password"
                rules={[
                  {
                    required: true,
                    message: formatMessage({
                      id: errors.password,
                    }),
                  },
                ]}
              >
                <Input
                  type="password"
                  placeholder={formatMessage({
                    id: placeholders.password,
                  })}
                />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: fields.email })}
                name="email"
                rules={[
                  {
                    required: true,
                    message: formatMessage({ id: errors.email }),
                  },
                ]}
              >
                <Input
                  type="email"
                  placeholder={formatMessage({
                    id: placeholders.email,
                  })}
                />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item label={formatMessage({ id: fields.firstName })} name="firstName">
                <Input
                  placeholder={formatMessage({
                    id: placeholders.firstName,
                  })}
                />
              </Form.Item>
            </Col>
          </Row>

          <Row>
            <Col span={16}>
              <Form.Item label={formatMessage({ id: fields.lastName })} name="lastName">
                <Input
                  placeholder={formatMessage({
                    id: placeholders.lastName,
                  })}
                />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item {...tailLayout}>
                <Button type="primary" htmlType="submit">
                  <FormattedMessage id={localeKeys.form.save} />
                </Button>
              </Form.Item>
            </Col>
          </Row>
        </Card>
      </PageHeaderWrapper>
    </Form>
  );
}
