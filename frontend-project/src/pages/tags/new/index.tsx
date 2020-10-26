import { PageHeaderWrapper } from '@ant-design/pro-layout';
import { Button, Col, Card, Form, Input, Row, Alert } from 'antd';
import { connect } from 'dva';
import { AnyAction, Dispatch } from 'redux';
import React, { useEffect, FC } from 'react';
import { formatMessage, FormattedMessage } from 'umi-plugin-react/locale';
import { Tag } from '@/services/definitions';
import { TagModelState } from '@/models/tag';

export interface TagNewFormProps {
  dispatch: Dispatch<AnyAction>;
  submitting: boolean;
  createdTag: TagModelState;
}
const layout = {
  labelCol: { span: 8 },
  wrapperCol: { span: 16 },
};

const tailLayout = {
  wrapperCol: { offset: 8, span: 16 },
};

export interface TagMessageProps {
  content: string;
}
const TagMessage = ({ content }: TagMessageProps) => (
  <Alert
    style={{
      marginLeft: 300,
      marginBottom: 24,
    }}
    message={content}
    type="error"
    showIcon
  />
);

const TagNewForm: FC<TagNewFormProps> = (props: TagNewFormProps) => {
  const [form] = Form.useForm();
  const handleSubmit = (value: Tag) => {
    const { dispatch } = props;
    dispatch({
      type: 'tag/create',
      payload: { ...value },
    });
  };

  useEffect(() => {}, []);

  return (
    <Form {...layout} form={form} onFinish={handleSubmit}>
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
              {props.createdTag.tag?.name && <TagMessage content={props.createdTag.tag?.name} />}
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

export default connect(state => ({ createdTag: (state as any).tag }))(TagNewForm);
