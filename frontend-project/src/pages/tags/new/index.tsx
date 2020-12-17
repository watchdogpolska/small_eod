import { PageHeaderWrapper } from '@ant-design/pro-layout';
import { Button, Col, Card, Form, Input, Row } from 'antd';
import { connect } from 'dva';
import { AnyAction, Dispatch } from 'redux';
import React, { useEffect, FC } from 'react';
import { formatMessage, FormattedMessage } from 'umi-plugin-react/locale';
import { Tag } from '@/services/definitions';
import { TagModelState } from '@/models/tag';

export interface TagNewFormProps {
  dispatch: Dispatch<AnyAction>;
  submitting: boolean;
  tagState: TagModelState;
}
const layout = {
  labelCol: { span: 8 },
  wrapperCol: { span: 16 },
};

const tailLayout = {
  wrapperCol: { offset: 8, span: 16 },
};
const TagNewForm: FC<TagNewFormProps> = (props: TagNewFormProps) => {
  const [form] = Form.useForm();

  const handleSubmit = (value: Tag) => {
    const { dispatch } = props;
    dispatch({
      type: 'tag/create',
      payload: { ...value },
    });
  };

  form.setFields(Object.entries(props?.tagState.tag).map(([name, errors]) => ({ name, errors })));
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

export default connect(state => ({ tagState: (state as any).tag }))(TagNewForm);
