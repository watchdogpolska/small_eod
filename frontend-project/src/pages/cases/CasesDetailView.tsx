import { PageHeaderWrapper } from '@ant-design/pro-layout';
import { Button, Col, Card, Form, Input, Row, Select, Space, Spin } from 'antd';
import { connect, useDispatch } from 'dva';
import React, { useEffect, useState } from 'react';
import { formatMessage, FormattedMessage } from 'umi-plugin-react/locale';
import { Institution, User, Tag, Case, Feature } from '@/services/definitions';
import { ReduxResourceState } from '@/utils/reduxModel';
import router from 'umi/router';
import { RouterTypes } from 'umi';
import { ServiceResponse } from '@/services/service';
import { openNotificationWithIcon } from '@/models/global';
import { localeKeys } from '../../locales/pl-PL';

interface CasesDetailViewProps {
  cases: ReduxResourceState<Case>;
  tags: ReduxResourceState<Tag>;
  users: ReduxResourceState<User>;
  institutions: Institution[];
  features: ReduxResourceState<Feature>;
  match: RouterTypes['match'] & { params: { id: string | undefined } };
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

function CasesDetailView({
  cases,
  tags,
  users,
  institutions,
  features,
  match,
}: CasesDetailViewProps) {
  const dispatch = useDispatch();
  const isEdit = Boolean(match.params.id);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const editedCase = cases.data.find(value => value.id === Number(match.params.id));
  const [form] = Form.useForm();

  function onRequestDone(response: ServiceResponse<Case>) {
    setIsSubmitting(false);
    if (response.status === 'success') {
      router.push('/cases');
    } else if (response.statusCode === 400) {
      form.setFields(
        Array.from(
          Object.entries(response.errorBody),
        ).map(([name, errors]: [string, Array<string>]) => ({ name, errors })),
      );
    } else {
      openNotificationWithIcon(
        'error',
        formatMessage({ id: localeKeys.error }),
        `${formatMessage({
          id: isEdit
            ? localeKeys.cases.detailView.errors.updateFailed
            : localeKeys.cases.detailView.errors.createFailed,
        })} ${response.errorText}`,
      );
    }
  }

  function onFinish() {
    if (isEdit) {
      dispatch({
        type: 'cases/update',
        payload: {
          ...form.getFieldsValue(),
          id: match.params.id,
          onResponse: onRequestDone,
        },
      });
    } else {
      dispatch({
        type: 'cases/create',
        payload: {
          ...form.getFieldsValue(),
          onResponse: onRequestDone,
        },
      });
    }
    setIsSubmitting(true);
  }

  useEffect(() => {
    dispatch({ type: 'tags/fetchAll' });
    dispatch({ type: 'users/fetchAll' });
    dispatch({ type: 'institutions/fetchAll' });
    dispatch({ type: 'features/fetchAll' });
    if (isEdit) dispatch({ type: 'cases/fetchOne', payload: { id: Number(match.params.id) } });
  }, []);

  if (
    cases.isLoading ||
    tags.isLoading ||
    users.isLoading ||
    features.isLoading ||
    (isEdit && !editedCase) ||
    isSubmitting
  ) {
    return (
      <Row justify="center">
        <Col>
          <Spin size="large" />
        </Col>
      </Row>
    );
  }
  if (isEdit) form.setFieldsValue(editedCase);

  return (
    <Form {...layout} form={form} onFinish={onFinish}>
      <PageHeaderWrapper
        content={formatMessage({
          id: isEdit
            ? localeKeys.cases.detailView.editPageHeaderContent
            : localeKeys.cases.detailView.newPageHeaderContent,
        })}
      >
        <Card bordered={false}>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: localeKeys.cases.fields.name })}
                name="name"
                rules={[
                  {
                    required: true,
                    message: formatMessage({ id: localeKeys.cases.detailView.errors.name }),
                  },
                ]}
              >
                <Input
                  placeholder={formatMessage({ id: localeKeys.cases.detailView.placeholders.name })}
                />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: localeKeys.cases.fields.comment })}
                name="comment"
                rules={[
                  {
                    required: true,
                    message: formatMessage({ id: localeKeys.cases.detailView.errors.comment }),
                  },
                ]}
              >
                <TextArea
                  rows={4}
                  placeholder={formatMessage({
                    id: localeKeys.cases.detailView.placeholders.comment,
                  })}
                />
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: localeKeys.cases.fields.tags })}
                name="tags"
                rules={[
                  {
                    required: true,
                    message: formatMessage({ id: localeKeys.cases.detailView.errors.tags }),
                  },
                ]}
              >
                <Select
                  mode="tags"
                  placeholder={formatMessage({ id: localeKeys.cases.detailView.placeholders.tags })}
                >
                  {tags.data.map(tag => (
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
                label={formatMessage({ id: localeKeys.cases.fields.features })}
                name="featureoptions"
                rules={[
                  {
                    required: true,
                    message: formatMessage({ id: localeKeys.cases.detailView.errors.features }),
                  },
                ]}
              >
                <Select
                  mode="multiple"
                  placeholder={formatMessage({
                    id: localeKeys.cases.detailView.placeholders.features,
                  })}
                >
                  {features.data.map(feature => (
                    <Option key={feature.id} value={feature.id}>
                      {feature.name}
                    </Option>
                  ))}
                </Select>
              </Form.Item>
            </Col>
          </Row>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: localeKeys.cases.fields.auditedInstitutions })}
                name="auditedInstitutions"
              >
                <Select
                  mode="multiple"
                  placeholder={formatMessage({
                    id: localeKeys.cases.detailView.placeholders.auditedInstitutions,
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
                label={formatMessage({ id: localeKeys.cases.fields.notifiedUsers })}
                name="notifiedUsers"
              >
                <Select
                  mode="multiple"
                  placeholder={formatMessage({
                    id: localeKeys.cases.detailView.placeholders.notifiedUsers,
                  })}
                >
                  {users.data.map(user => (
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
                label={formatMessage({ id: localeKeys.cases.fields.responsibleUsers })}
                name="responsibleUsers"
              >
                <Select
                  mode="multiple"
                  placeholder={formatMessage({
                    id: localeKeys.cases.detailView.placeholders.responsibleUsers,
                  })}
                >
                  {users.data.map(user => (
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
                <Space>
                  <Button type="default" htmlType="reset">
                    <FormattedMessage id={localeKeys.form.reset} />
                  </Button>
                  <Button type="primary" htmlType="submit">
                    <FormattedMessage id={localeKeys.form.save} />
                  </Button>
                </Space>
              </Form.Item>
            </Col>
          </Row>
        </Card>
      </PageHeaderWrapper>
    </Form>
  );
}

export default connect((props: CasesDetailViewProps) => props)(CasesDetailView);
