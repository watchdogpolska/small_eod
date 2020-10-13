import { PageHeaderWrapper } from '@ant-design/pro-layout';
import { Button, Col, Card, Form, Input, Row } from 'antd';
import { connect } from 'dva';
import React, { useEffect, FC } from 'react';
import { formatMessage, FormattedMessage } from 'umi-plugin-react/locale';
import { Tag } from '@/services/definitions';

interface TagNewFormProps {
  name: string;
  dispatch: Function;
}

const layout = {
  labelCol: { span: 8 },
  wrapperCol: { span: 16 },
};

const tailLayout = {
  wrapperCol: { offset: 8, span: 16 },
};

const TagNewForm: FC<TagNewFormProps> = ({ dispatch }) => {
  const [form] = Form.useForm();
  const onSubmit = (value: Tag) => {
    dispatch({
      type: 'tags/create',
      payload: { ...value },
    });
  };
  const onFinish = (): void => {
    onSubmit(form.getFieldsValue() as Tag);
  };

  useEffect(() => {}, []);

  return (
    <Form {...layout} form={form} onFinish={onFinish}>
      <PageHeaderWrapper content={formatMessage({ id: 'tags-new.page-header-content' })}>
        <Card bordered={false}>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: 'tags-new.form.name.label' })}
                name="name"
                rules={[
                  {
                    required: true,
                    message: formatMessage({ id: 'tags-new.form.name.required-error' }),
                  },
                ]}
              >
                <Input placeholder={formatMessage({ id: 'tags-new.form.name.placeholder' })} />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item {...tailLayout}>
                <Button type="primary" htmlType="submit">
                  <FormattedMessage id="tags-new.form.save.label" />
                </Button>
              </Form.Item>
            </Col>
          </Row>
        </Card>
      </PageHeaderWrapper>
    </Form>
  );
};

export default connect(() => ({}))(TagNewForm);
