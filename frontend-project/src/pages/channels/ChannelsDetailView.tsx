import { PageHeaderWrapper } from '@ant-design/pro-layout';
import { Button, Col, Card, Form, Input, Row, Space, Spin, Switch } from 'antd';
import React, { useEffect, useState } from 'react';
import { formatMessage, FormattedMessage } from 'umi-plugin-react/locale';
import router from 'umi/router';
import { localeKeys } from '../../locales/pl-PL';
import { getFormErrorFromPromiseError } from '@/utils/getFormErrorFromPromiseError';
import { DetailMatchParam } from '@/models/connect';
import { ChannelsService } from '@/services/channels';
import { Channel } from '@/services/definitions';

const layout = {
  labelCol: { span: 8 },
  wrapperCol: { span: 16 },
};

const tailLayout = {
  wrapperCol: { offset: 8, span: 16 },
};

export default function ChannelsDetailView({ match }: DetailMatchParam) {
  const isEdit = Boolean(match.params.id);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [editedItem, setEditedItem] = useState<Channel | undefined>();
  const [form] = Form.useForm();
  const {
    fields,
    detailView: { editPageHeaderContent, newPageHeaderContent, placeholders, errors },
  } = localeKeys.channels;

  useEffect(() => {
    if (isEdit)
      ChannelsService.fetchOne(Number(match.params.id)).then(response => setEditedItem(response));
  }, []);

  function onError(response: any) {
    setIsSubmitting(false);
    if (response?.statusCode === 400) {
      form.setFields(getFormErrorFromPromiseError(response));
    }
  }

  function onSubmit() {
    const action = isEdit ? ChannelsService.update : ChannelsService.create;
    action({
      ...(form.getFieldsValue() as Channel),
      id: Number(match.params.id),
    })
      .then(() => {
        router.push('/channels');
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
              <Form.Item
                label={formatMessage({ id: fields.email })}
                name="email"
                valuePropName="checked"
              >
                <Switch />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: fields.epuap })}
                name="epuap"
                valuePropName="checked"
              >
                <Switch />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: fields.city })}
                name="city"
                valuePropName="checked"
              >
                <Switch />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: fields.street })}
                name="street"
                valuePropName="checked"
              >
                <Switch />
              </Form.Item>
            </Col>
          </Row>

          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: fields.houseNo })}
                name="houseNo"
                valuePropName="checked"
              >
                <Switch />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: fields.flatNo })}
                name="flatNo"
                valuePropName="checked"
              >
                <Switch />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: fields.postalCode })}
                name="postalCode"
                valuePropName="checked"
              >
                <Switch />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: fields.voivodeship })}
                name="voivodeship"
                valuePropName="checked"
              >
                <Switch />
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
