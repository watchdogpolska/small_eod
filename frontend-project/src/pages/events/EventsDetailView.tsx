import { PageHeaderWrapper } from '@ant-design/pro-layout';
import { Button, Card, Col, DatePicker, Form, Input, Row, Select, Space, Spin } from 'antd';
import { connect, useDispatch } from 'dva';
import moment from 'moment';
import React, { useEffect, useState } from 'react';
import { RouterTypes } from 'umi';
import { formatMessage, FormattedMessage } from 'umi-plugin-react/locale';
import router from 'umi/router';
import { localeKeys } from '../../locales/pl-PL';
import { openNotificationWithIcon } from '../../models/global';
import { Case, Event } from '../../services/definitions';
import { ServiceResponse } from '../../services/service';
import { ReduxResourceState } from '../../utils/reduxModel';

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
  const resourceId = match.params.id;
  const isEdit = Boolean(resourceId);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const editedEvent = events.data.find(value => value.id === Number(match.params.id));
  const [form] = Form.useForm();
  const {
    fields,
    detailView: { errors, placeholders, editPageHeaderContent, newPageHeaderContent },
  } = localeKeys.events;

  function onRequestDone(response: ServiceResponse<Event>) {
    setIsSubmitting(false);
    if (response.status === 'success') {
      router.push('/events');
    } else if (response.statusCode === 400) {
      form.setFields(
        Array.from(
          Object.entries(response.errorBody),
        ).map(([name, formErrors]: [string, Array<string>]) => ({ name, formErrors })),
      );
    } else {
      openNotificationWithIcon(
        'error',
        formatMessage({ id: localeKeys.error }),
        `${formatMessage({
          id: isEdit ? errors.updateFailed : errors.createFailed,
        })} ${response.errorText}`,
      );
    }
  }

  function onFinish() {
    dispatch({
      type: `events/${isEdit ? 'update' : 'create'}`,
      payload: {
        ...form.getFieldsValue(),
        id: resourceId,
        onResponse: onRequestDone,
      },
    });
    setIsSubmitting(true);
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
      date: moment(editedEvent.date),
    });

  return (
    <Form {...layout} form={form} onFinish={onFinish}>
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
                label={formatMessage({ id: fields.case })}
                name="case"
                rules={[
                  {
                    required: true,
                    message: formatMessage({ id: errors.case }),
                  },
                ]}
              >
                <Select
                  placeholder={formatMessage({
                    id: placeholders.case,
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
                label={formatMessage({ id: fields.date })}
                name="date"
                rules={[
                  {
                    required: true,
                    message: formatMessage({ id: errors.date }),
                  },
                ]}
              >
                <DatePicker
                  showTime
                  placeholder={formatMessage({
                    id: placeholders.date,
                  })}
                  style={{
                    width: '100%',
                  }}
                />
              </Form.Item>
            </Col>
          </Row>

          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: fields.comment })}
                name="comment"
                rules={[
                  {
                    required: true,
                    message: formatMessage({ id: errors.comment }),
                  },
                ]}
              >
                <TextArea
                  rows={4}
                  placeholder={formatMessage({
                    id: placeholders.comment,
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
