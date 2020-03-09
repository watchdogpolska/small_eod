import { PageHeaderWrapper } from '@ant-design/pro-layout';
import { Button, Card, Form, Input, Row, Select } from 'antd';
import React from 'react';
import { formatMessage, FormattedMessage } from 'umi-plugin-react/locale';

const { TextArea } = Input;

const CasesNewForm = () => {
  const [form] = Form.useForm();

  const onSubmit = () => {
    form.submit();
  };

  return (
    <Form form={form}>
      <PageHeaderWrapper content={formatMessage({ id: 'cases-new.page-header-content' })}>
        <Card bordered={false}>
          <Row>
            <Form.Item
              label={formatMessage({ id: 'cases-new.form.name.label' })}
              name="name"
              rules={[
                {
                  required: true,
                  message: formatMessage({ id: 'cases-new.form.name.required-error' }),
                },
              ]}
            >
              <Input placeholder={formatMessage({ id: 'cases-new.form.name.placeholder' })} />
            </Form.Item>
          </Row>
          <Row>
            <Form.Item
              label={formatMessage({ id: 'cases-new.form.comment.label' })}
              name="comment"
              rules={[
                {
                  required: true,
                  message: formatMessage({ id: 'cases-new.form.comment.required-error' }),
                },
              ]}
            >
              <TextArea
                rows={4}
                placeholder={formatMessage({ id: 'cases-new.form.comment.placeholder' })}
              />
            </Form.Item>
          </Row>
          <Row>
            <Form.Item
              label={formatMessage({ id: 'cases-new.form.tags.label' })}
              name="tags"
              rules={[
                {
                  required: true,
                  message: formatMessage({ id: 'cases-new.form.tags.required-error' }),
                },
              ]}
            >
              <Select
                mode="tags"
                placeholder={formatMessage({ id: 'cases-new.form.tags.placeholder' })}
              />
            </Form.Item>
          </Row>
          <Row>
            <Form.Item
              label={formatMessage({ id: 'cases-new.form.features.label' })}
              name="features"
              rules={[
                {
                  required: true,
                  message: formatMessage({ id: 'cases-new.form.features.required-error' }),
                },
              ]}
            >
              <Select
                mode="multiple"
                placeholder={formatMessage({ id: 'cases-new.form.features.placeholder' })}
              />
            </Form.Item>
          </Row>
          <Row>
            <Form.Item
              label={formatMessage({ id: 'cases-new.form.audited-institution.label' })}
              name="audited-institution"
            >
              <Select
                mode="multiple"
                placeholder={formatMessage({
                  id: 'cases-new.form.audited-institution.placeholder',
                })}
              />
            </Form.Item>
          </Row>
          <Row>
            <Form.Item
              label={formatMessage({ id: 'cases-new.form.notified-users.label' })}
              name="notified-users"
            >
              <Select
                mode="multiple"
                placeholder={formatMessage({ id: 'cases-new.form.notified-users.placeholder' })}
              />
            </Form.Item>
          </Row>
          <Row>
            <Form.Item
              label={formatMessage({ id: 'cases-new.form.responsible-users.label' })}
              name="notified-users"
            >
              <Select
                mode="multiple"
                placeholder={formatMessage({ id: 'cases-new.form.responsible-users.placeholder' })}
              />
            </Form.Item>
          </Row>
          <Row>
            <Button type="primary" onClick={onSubmit}>
              <FormattedMessage id="cases-new.form.save.label" />
            </Button>
          </Row>
        </Card>
      </PageHeaderWrapper>
    </Form>
  );
};

export default CasesNewForm;
