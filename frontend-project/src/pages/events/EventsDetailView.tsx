import { PageHeaderWrapper } from '@ant-design/pro-layout';
import { Button, Col, Card, Form, Input, Row, Select, Space, Spin } from 'antd';
import { connect, useDispatch } from 'dva';
import React, { useEffect, useState } from 'react';
import { formatMessage, FormattedMessage } from 'umi-plugin-react/locale';
import { Event, Case } from '@/services/definitions';
import { ReduxResourceState } from '@/utils/reduxModel';
import router from 'umi/router';
import { localeKeys } from '../../locales/pl-PL';
import { RouterTypes } from 'umi';
import { ServiceResponse } from '@/services/service';
import { openNotificationWithIcon } from '@/models/global';

interface EventsDetailViewProps {
  events: ReduxResourceState<Event>;
  cases: ReduxResourceState<Case>;
  match: RouterTypes['match'] & { params: { id: string | undefined } };
}

const { TextArea } = Input;
const { Option } = Select;

const layout = {
  labelCol: { span: 8 },
  wrapperCol: { span: 16 },
};

const tailLayout = {
  wrapperCol: { offset: 8, span: 16 },
};

function EventsDetailView({ events, cases, match }: EventsDetailViewProps) {
  const dispatch = useDispatch();
  const isEdit = Boolean(match.params.id);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const editedEvent = events.data.find(value => value.id === Number(match.params.id));
  const [form] = Form.useForm();
  function onRequestDone(response: ServiceResponse<Event>) {
    setIsSubmitting(false);
    if (response.status === 'success') {
      router.push('/events');
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
            ? localeKeys.events.detailView.errors.updateFailed
            : localeKeys.events.detailView.errors.createFailed,
        })} ${response.errorText}`,
      );
    }
  }

  function onFinish() {
    if (isEdit) {
      dispatch({
        type: 'events/update',
        payload: {
          ...form.getFieldsValue(),
          id: match.params.id,
          onResponse: onRequestDone,
        },
      });
    } else {
      dispatch({
        type: 'events/create',
        payload: {
          ...form.getFieldsValue(),
          onResponse: onRequestDone,
        },
      });
    }
    setIsSubmitting(true);
  }

  function toDatetimeLocal(date: Date) {
    const pad = (number: Number) => String(number).padStart(2, '0');
    const YYYY = date.getFullYear();
    const MM = pad(date.getUTCMonth() + 1);
    const DD = pad(date.getUTCDate());
    const HH = pad(date.getUTCHours());
    const II = pad(date.getUTCMinutes());
    const SS = pad(date.getUTCSeconds());
    return `${YYYY}-${MM}-${DD}T${HH}:${II}:${SS}`;
  }

  useEffect(() => {
    dispatch({ type: 'cases/fetchAll' });
    if (isEdit) dispatch({ type: 'events/fetchOne', payload: { id: Number(match.params.id) } });
  }, []);

  if (events.isLoading || cases.isLoading || (isEdit && !editedEvent) || isSubmitting) {
    return (
      <Row justify="center">
        <Col>
          <Spin size="large" />
        </Col>
      </Row>
    );
  }
  if (isEdit)
    form.setFieldsValue({
      ...editedEvent,
      date: toDatetimeLocal(new Date(editedEvent.date)),
    });

  return (
    <Form {...layout} form={form} onFinish={onFinish}>
      <PageHeaderWrapper
        content={formatMessage({
          id: isEdit
            ? localeKeys.events.detailView.editPageHeaderContent
            : localeKeys.events.detailView.newPageHeaderContent,
        })}
      >
        <Card bordered={false}>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: localeKeys.events.fields.name })}
                name="name"
                rules={[
                  {
                    required: true,
                    message: formatMessage({ id: localeKeys.events.detailView.errors.name }),
                  },
                ]}
              >
                <Input
                  placeholder={formatMessage({
                    id: localeKeys.events.detailView.placeholders.name,
                  })}
                />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: localeKeys.events.fields.case })}
                name="case"
                rules={[
                  {
                    required: true,
                    message: formatMessage({ id: localeKeys.events.detailView.errors.case }),
                  },
                ]}
              >
                <Select
                  placeholder={formatMessage({
                    id: localeKeys.events.detailView.placeholders.case,
                  })}
                >
                  {cases.data.map(singleCase => (
                    <Option key={singleCase.id} value={singleCase.id}>
                      {singleCase.name}
                    </Option>
                  ))}
                </Select>
              </Form.Item>
            </Col>
          </Row>

          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: localeKeys.events.fields.date })}
                name="date"
                rules={[
                  {
                    required: true,
                    message: formatMessage({ id: localeKeys.events.detailView.errors.date }),
                  },
                ]}
              >
                <Input
                  type="datetime-local"
                  placeholder={formatMessage({
                    id: localeKeys.events.detailView.placeholders.date,
                  })}
                />
              </Form.Item>
            </Col>
          </Row>

          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: localeKeys.events.fields.comment })}
                name="comment"
                rules={[
                  {
                    required: true,
                    message: formatMessage({ id: localeKeys.events.detailView.errors.comment }),
                  },
                ]}
              >
                <TextArea
                  rows={4}
                  placeholder={formatMessage({
                    id: localeKeys.events.detailView.placeholders.comment,
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

export default connect((props: EventsDetailViewProps) => props)(EventsDetailView);
