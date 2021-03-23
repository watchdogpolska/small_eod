import { PageHeaderWrapper } from '@ant-design/pro-layout';
import { Button, Col, Card, Form, Row, Spin, Input } from 'antd';
import React, { useEffect, useState } from 'react';
import { formatMessage, FormattedMessage } from 'umi-plugin-react/locale';
import router from 'umi/router';

import { localeKeys } from '../../locales/pl-PL';
import { getFormErrorFromPromiseError } from '@/utils/getFormErrorFromPromiseError';
import { DetailMatchParam } from '@/models/connect';
import { Note } from '@/services/definitions';
import { NotesService } from '@/services/notes';
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

export default function NotesDetailView({ match }: DetailMatchParam) {
  const isEdit = Boolean(match.params.id);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [editedItem, setEditedItem] = useState<Note | undefined>();
  const [form] = Form.useForm();
  const {
    fields,
    detailView: { editPageHeaderContent, newPageHeaderContent, placeholders, errors },
  } = localeKeys.notes;

  useEffect(() => {
    if (isEdit) NotesService.fetchOne(match.params.id).then(response => setEditedItem(response));
  }, []);

  function onError(response: any) {
    setIsSubmitting(false);
    if (response?.statusCode === 400) {
      form.setFields(getFormErrorFromPromiseError(response));
    }
  }

  function onSubmit() {
    const action = isEdit ? NotesService.update : NotesService.create;
    action({
      ...(form.getFieldsValue() as Note),
      id: Number(match.params.id),
    })
      .then(() => router.push('/notes/list'))
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
                  placeholder={formatMessage({
                    id: placeholders.case,
                  })}
                  mode={undefined}
                  autocompleteFunction={AutocompleteService.cases}
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
