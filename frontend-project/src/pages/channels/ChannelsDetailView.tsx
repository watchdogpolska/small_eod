import { PageHeaderWrapper } from '@ant-design/pro-layout';
import { Button, Col, Card, Form, Input, Row, Space, Spin, Switch } from 'antd';
import { connect, useDispatch } from 'dva';
import React, { useEffect, useState } from 'react';
import { formatMessage, FormattedMessage } from 'umi-plugin-react/locale';
import { Channel } from '@/services/definitions';
import { ReduxResourceState } from '@/utils/reduxModel';
import router from 'umi/router';
import { localeKeys } from '../../locales/pl-PL';
import { RouterTypes } from 'umi';
import { ServiceResponse } from '@/services/service';
import { openNotificationWithIcon } from '@/models/global';

interface ChannelsDetailViewProps {
  channels: ReduxResourceState<Channel>;
  match: RouterTypes['match'] & { params: { id: string | undefined } };
}

const layout = {
  labelCol: { span: 8 },
  wrapperCol: { span: 16 },
};

const tailLayout = {
  wrapperCol: { offset: 8, span: 16 },
};

function ChannelsDetailView({ channels, match }: ChannelsDetailViewProps) {
  const dispatch = useDispatch();
  const isEdit = Boolean(match.params.id);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const editedChannel = channels.data.find(value => value.id === Number(match.params.id));
  const [form] = Form.useForm();
  function onRequestDone(response: ServiceResponse<Channel>) {
    setIsSubmitting(false);
    if (response.status === 'success') {
      router.push('/channels/list');
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
            ? localeKeys.channels.detailView.errors.updateFailed
            : localeKeys.channels.detailView.errors.createFailed,
        })} ${response.errorText}`,
      );
    }
  }

  function onFinish() {
    if (isEdit) {
      dispatch({
        type: 'channels/update',
        payload: {
          ...form.getFieldsValue(),
          id: match.params.id,
          onResponse: onRequestDone,
        },
      });
    } else {
      dispatch({
        type: 'channels/create',
        payload: {
          ...form.getFieldsValue(),
          onResponse: onRequestDone,
        },
      });
    }
    setIsSubmitting(true);
  }

  useEffect(() => {
    if (isEdit) dispatch({ type: 'channels/fetchOne', payload: { id: Number(match.params.id) } });
  }, []);

  if (channels.isLoading || (isEdit && !editedChannel) || isSubmitting) {
    return (
      <Row justify="center">
        <Col>
          <Spin size="large" />
        </Col>
      </Row>
    );
  }
  if (isEdit) form.setFieldsValue(editedChannel);

  return (
    <Form {...layout} form={form} onFinish={onFinish}>
      <PageHeaderWrapper
        content={formatMessage({
          id: isEdit
            ? localeKeys.channels.detailView.editPageHeaderContent
            : localeKeys.channels.detailView.newPageHeaderContent,
        })}
      >
        <Card bordered={false}>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: localeKeys.channels.fields.name })}
                name="name"
                rules={[
                  {
                    required: true,
                    message: formatMessage({ id: localeKeys.channels.detailView.errors.name }),
                  },
                ]}
              >
                <Input
                  placeholder={formatMessage({
                    id: localeKeys.channels.detailView.placeholders.name,
                  })}
                />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: localeKeys.channels.fields.email })}
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
                label={formatMessage({ id: localeKeys.channels.fields.epuap })}
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
                label={formatMessage({ id: localeKeys.channels.fields.city })}
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
                label={formatMessage({ id: localeKeys.channels.fields.street })}
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
                label={formatMessage({ id: localeKeys.channels.fields.houseNo })}
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
                label={formatMessage({ id: localeKeys.channels.fields.flatNo })}
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
                label={formatMessage({ id: localeKeys.channels.fields.postalCode })}
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
                label={formatMessage({ id: localeKeys.channels.fields.voivodeship })}
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

export default connect((props: ChannelsDetailViewProps) => props)(ChannelsDetailView);
