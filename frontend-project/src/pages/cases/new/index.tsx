import { PageHeaderWrapper } from '@ant-design/pro-layout';
import { Button, Col, Card, Form, Input, Row, Select } from 'antd';
import { connect } from 'dva';
import React, { useEffect, FunctionComponent } from 'react';
import { formatMessage, FormattedMessage } from 'umi-plugin-react/locale';
import { Institution } from '@/models/institutions';
import { User } from '@/models/users';

interface Tag {
  name: string;
}

interface CasesNewFormProps {
  tags: Tag[];
  users: User[];
  institutions: Institution[];
  dispatch: Function;
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

const CasesNewForm: FunctionComponent<CasesNewFormProps> = ({
  tags,
  users,
  institutions,
  dispatch,
}) => {
  const [form] = Form.useForm();

  const onSubmit = () => {
    form.submit();
  };
  useEffect(() => {
    dispatch({ type: 'tags/fetchAll' });
    dispatch({ type: 'users/fetchAll' });
    dispatch({ type: 'institutions/fetchAll' });
  }, []);

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
                >
                  {tags.map(tag => (
                    <Option key={tag.name} value={tag.name}>
                      {tag.name}
                    </Option>
                  ))}
                </Select>
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
                >
                  {institutions.map(institution => (
                    <Option key={institution.id} value={institution.id}>
                      {institution.name}
                    </Option>
                  ))}
                </Select>
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
                >
                  {users.map(user => (
                    <Option key={user.id} value={user.id}>
                      {user.username}
                    </Option>
                  ))}
                </Select>
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: 'cases-new.form.responsible-users.label' })}
                name="responsible-users"
              >
                <Select
                  mode="multiple"
                  placeholder={formatMessage({
                    id: 'cases-new.form.responsible-users.placeholder',
                  })}
                >
                  {users.map(user => (
                    <Option key={user.id} value={user.id}>
                      {user.username}
                    </Option>
                  ))}
                </Select>
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

export default connect(({ tags, users, institutions }: any) => ({ tags, users, institutions }))(
  CasesNewForm,
);
