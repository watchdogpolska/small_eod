import { getFormErrorFromPromiseError } from '@/utils/getFormErrorFromPromiseError';
import { PageHeaderWrapper } from '@ant-design/pro-layout';
import { Button, Card, Col, DatePicker, Form, Input, Row, Spin } from 'antd';
import moment from 'moment';
import React, { useEffect, useState } from 'react';
import { formatMessage, FormattedMessage } from 'umi-plugin-react/locale';
import router from 'umi/router';
import { localeKeys } from '../../locales/pl-PL';
import { DetailMatchParam } from '@/models/connect';
import { Event } from '@/services/definitions';
import { EventsService } from '@/services/events';
import { FetchSelect } from '@/components/FetchSelect';
import { AutocompleteService } from '@/services/autocomplete';

const { TextArea } = Input;

const layout = {
  labelCol: { span: 8 },
  wrapperCol: { span: 16 },
};

const tailLayout = {
  wrapperCol: { offset: 8, span: 16 },
};

export default function EventsDetailView({ match }: DetailMatchParam) {
  const resourceId = match.params.id;
  const isEdit = Boolean(resourceId);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [editedItem, setEditedItem] = useState<Event | undefined>();
  const [form] = Form.useForm();
  const {
    fields,
    detailView: { errors, placeholders, editPageHeaderContent, newPageHeaderContent },
  } = localeKeys.events;

  useEffect(() => {
    if (isEdit)
      EventsService.fetchOne(Number(match.params.id)).then(response => setEditedItem(response));
  }, []);

  function onError(response: any) {
    setIsSubmitting(false);
    if (response?.statusCode === 400) {
      form.setFields(getFormErrorFromPromiseError(response));
    }
  }

  function onSubmit() {
    const action = isEdit ? EventsService.update : EventsService.create;
    action({
      ...(form.getFieldsValue() as Event),
      id: Number(match.params.id),
    })
      .then(() => {
        router.push('/events');
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
  if (isEdit)
    form.setFieldsValue({
      ...editedItem,
      date: moment(editedItem.date),
    });

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
                label={formatMessage({ id: fields.case })}
                name="case"
                rules={[
                  {
                    required: true,
                    message: formatMessage({ id: errors.case }),
                  },
                ]}
              >
                <FetchSelect
                  mode={undefined}
                  placeholder={formatMessage({
                    id: placeholders.case,
                  })}
                  autocompleteFunction={AutocompleteService.cases}
                />
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
