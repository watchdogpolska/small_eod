import { PageHeaderWrapper } from '@ant-design/pro-layout';
import { Button, Col, Card, Form, Input, Row, Spin } from 'antd';
import React, { useEffect, useState } from 'react';
import { formatMessage, FormattedMessage } from 'umi-plugin-react/locale';
import router from 'umi/router';
import { localeKeys } from '../../locales/pl-PL';
import { getFormErrorFromPromiseError } from '../../utils/getFormErrorFromPromiseError';
import { DetailMatchParam } from '../../models/connect';
import { FetchSelect } from '../../components/FetchSelect';
import { CasesService } from '../../services/cases';
import { Case } from '../../services/definitions';
import { AutocompleteService } from '../../services/autocomplete';

const { TextArea } = Input;

const layout = {
  labelCol: { span: 8 },
  wrapperCol: { span: 16 },
};

const tailLayout = {
  wrapperCol: { offset: 8, span: 16 },
};

export default function CasesDetailView({ match }: DetailMatchParam) {
  const isEdit = Boolean(match.params.id);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [editedItem, setEditedItem] = useState<Case | undefined>();
  const [form] = Form.useForm();
  const {
    fields,
    detailView: { editPageHeaderContent, newPageHeaderContent, placeholders, errors },
  } = localeKeys.cases;

  useEffect(() => {
    if (isEdit)
      CasesService.fetchOne(Number(match.params.id)).then(response => setEditedItem(response));
  }, []);

  function onError(response: any) {
    setIsSubmitting(false);
    if (response?.statusCode === 400) {
      form.setFields(getFormErrorFromPromiseError(response));
    }
  }
  function onSubmit() {
    const action = isEdit ? CasesService.update : CasesService.create;
    action({
      ...(form.getFieldsValue() as Case),
      id: Number(match.params.id),
    })
      .then(() => {
        router.push('/cases');
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
                <Input placeholder={formatMessage({ id: placeholders.name })} />
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
              <Form.Item
                label={formatMessage({ id: fields.tags })}
                name="tags"
                rules={[
                  {
                    required: true,
                    message: formatMessage({ id: errors.tags }),
                  },
                ]}
              >
                <FetchSelect
                  mode="tags"
                  placeholder={formatMessage({ id: placeholders.tags })}
                  autocompleteFunction={AutocompleteService.tags}
                />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: fields.featureOptions })}
                name="featureoptions"
                rules={[
                  {
                    required: true,
                    message: formatMessage({ id: errors.featureOptions }),
                  },
                ]}
              >
                <FetchSelect
                  mode="multiple"
                  placeholder={formatMessage({
                    id: placeholders.featureOptions,
                  })}
                  autocompleteFunction={AutocompleteService.featureOptions}
                />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: fields.auditedInstitutions })}
                name="auditedInstitutions"
              >
                <FetchSelect
                  mode="multiple"
                  placeholder={formatMessage({
                    id: placeholders.auditedInstitutions,
                  })}
                  autocompleteFunction={AutocompleteService.institutions}
                />
              </Form.Item>
            </Col>
          </Row>

          <Row>
            <Col span={16}>
              <Form.Item label={formatMessage({ id: fields.notifiedUsers })} name="notifiedUsers">
                <FetchSelect
                  mode="multiple"
                  placeholder={formatMessage({
                    id: placeholders.notifiedUsers,
                  })}
                  autocompleteFunction={AutocompleteService.users}
                  labelField="username"
                />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: fields.responsibleUsers })}
                name="responsibleUsers"
              >
                <FetchSelect
                  mode="multiple"
                  placeholder={formatMessage({
                    id: placeholders.responsibleUsers,
                  })}
                  autocompleteFunction={AutocompleteService.users}
                  labelField="username"
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
