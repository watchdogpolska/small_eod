import { PageHeaderWrapper } from '@ant-design/pro-layout';
import { Button, Col, Card, Form, Input, Row, Select } from 'antd';
import React from 'react';
import { formatMessage, FormattedMessage } from 'umi-plugin-react/locale';

const { TextArea } = Input;

const layout = {
  labelCol: { span: 8 },
  wrapperCol: { span: 16 },
};

const tailLayout = {
  wrapperCol: { offset: 8, span: 16 },
};

const CasesNewForm = () => {
  const [form] = Form.useForm();

  const onSubmit = () => {
    form.submit();
  };

  return (
    <Form {...layout} form={form}>
      <PageHeaderWrapper content={formatMessage({ id: 'cases-new.page-header-content' })}>
        <Card bordered={false}>
          <Row>
            <Col span={16}>
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
            </Col>
          </Row>
          <Row>
            <Col span={16}>
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
            </Col>
          </Row>
          <Row>
            <Col span={16}>
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
            </Col>
          </Row>
          <Row>
            <Col span={16}>
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
            </Col>
          </Row>
          <Row>
            <Col span={16}>
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
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: 'cases-new.form.notified-users.label' })}
                name="notified-users"
              >
                <Select
                  mode="multiple"
                  placeholder={formatMessage({ id: 'cases-new.form.notified-users.placeholder' })}
                />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: 'cases-new.form.responsible-users.label' })}
                name="notified-users"
              >
                <Select
                  mode="multiple"
                  placeholder={formatMessage({
                    id: 'cases-new.form.responsible-users.placeholder',
                  })}
                />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item {...tailLayout}>
                <Button type="primary" onClick={onSubmit}>
                  <FormattedMessage id="cases-new.form.save.label" />
                </Button>
              </Form.Item>
            </Col>
          </Row>
        </Card>
      </PageHeaderWrapper>
    </Form>
  );
};

export default CasesNewForm;
