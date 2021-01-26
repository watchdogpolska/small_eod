import { PageHeaderWrapper } from '@ant-design/pro-layout';
import { Button, Col, Card, Form, Input, Row, Select } from 'antd';
import React, { FC } from 'react';
import { formatMessage, FormattedMessage } from 'umi';

const layout = {
  labelCol: { span: 8 },
  wrapperCol: { span: 16 },
};

const tailLayout = {
  wrapperCol: { offset: 8, span: 16 },
};

const InstitutionsNewForm: FC = () => {
  const [form] = Form.useForm();

  const onSubmit = () => {
    form.submit();
  };

  return (
    <Form {...layout} form={form}>
      <PageHeaderWrapper content={formatMessage({ id: 'institutions-new.page-header-content' })}>
        <Card bordered={false}>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: 'institutions-new.form.name.label' })}
                name="name"
                rules={[
                  {
                    required: true,
                    message: formatMessage({ id: 'institutions-new.form.name.required-error' }),
                  },
                ]}
              >
                <Input
                  placeholder={formatMessage({ id: 'institutions-new.form.name.placeholder' })}
                />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: 'institutions-new.form.administrative-division.label' })}
                name="administrative-division"
                rules={[
                  {
                    required: true,
                    message: formatMessage({
                      id: 'institutions-new.form.administrative-division.required-error',
                    }),
                  },
                ]}
              >
                <Select
                  placeholder={formatMessage({
                    id: 'institutions-new.form.administrative-division.placeholder',
                  })}
                />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: 'institutions-new.form.address.label' })}
                name="address"
                rules={[
                  {
                    required: true,
                    message: formatMessage({ id: 'institutions-new.form.address.required-error' }),
                  },
                ]}
              >
                <Select
                  placeholder={formatMessage({ id: 'institutions-new.form.address.placeholder' })}
                />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: 'institutions-new.form.external-identifier.label' })}
                name="external-identifier"
                rules={[
                  {
                    required: true,
                    message: formatMessage({
                      id: 'institutions-new.form.external-identifier.required-error',
                    }),
                  },
                ]}
              >
                <Select
                  placeholder={formatMessage({
                    id: 'institutions-new.form.external-identifier.placeholder',
                  })}
                />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item {...tailLayout}>
                <Button type="primary" onClick={onSubmit}>
                  <FormattedMessage id="institutions-new.form.save.label" />
                </Button>
              </Form.Item>
            </Col>
          </Row>
        </Card>
      </PageHeaderWrapper>
    </Form>
  );
};

export default InstitutionsNewForm;
