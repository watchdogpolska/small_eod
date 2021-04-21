import { PageHeaderWrapper } from '@ant-design/pro-layout';
import { Button, Card, Col, Form, Input, Row, Spin } from 'antd';
import React, { useEffect, useState } from 'react';
import { formatMessage, FormattedMessage } from 'umi-plugin-react/locale';
import router from 'umi/router';
import { FetchSelect } from '../../components/FetchSelect';
import { localeKeys } from '../../locales/pl-PL';
import { DetailMatchParam } from '../../models/connect';
import { AutocompleteService } from '../../services/autocomplete';
import { Institution } from '../../services/definitions';
import { InstitutionsService } from '../../services/institutions';
import { getFormErrorFromPromiseError } from '../../utils/getFormErrorFromPromiseError';

const { TextArea } = Input;

const layout = {
  labelCol: { span: 8 },
  wrapperCol: { span: 16 },
};

const tailLayout = {
  wrapperCol: { offset: 8, span: 16 },
};

export default function InstitutionsDetailView({ match }: DetailMatchParam) {
  const isEdit = Boolean(match.params.id);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [editedItem, setEditedItem] = useState<Institution | undefined>();
  const [form] = Form.useForm();
  const {
    fields,
    detailView: { editPageHeaderContent, newPageHeaderContent, placeholders, errors },
  } = localeKeys.institutions;

  useEffect(() => {
    if (isEdit)
      InstitutionsService.fetchOne(Number(match.params.id)).then(response =>
        setEditedItem(response),
      );
  }, []);

  function onError(response: any) {
    setIsSubmitting(false);
    if (response?.statusCode === 400) {
      form.setFields(getFormErrorFromPromiseError(response));
    }
  }

  function onSubmit() {
    const action = isEdit ? InstitutionsService.update : InstitutionsService.create;
    action({
      ...(form.getFieldsValue() as Institution),
      id: Number(match.params.id),
    })
      .then(() => {
        router.push('/institutions');
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
                label={formatMessage({ id: fields.administrativeUnit })}
                name="administrativeUnit"
                rules={[
                  {
                    required: true,
                    message: formatMessage({ id: errors.administrativeUnit }),
                  },
                ]}
              >
                <FetchSelect
                  mode={undefined}
                  placeholder={formatMessage({
                    id: placeholders.administrativeUnit,
                  })}
                  autocompleteFunction={AutocompleteService.administrativeUnits}
                />
              </Form.Item>
            </Col>
          </Row>

          <Row>
            <Col span={16}>
              <Form.Item label={formatMessage({ id: fields.email })} name="email">
                <Input type="email" placeholder={formatMessage({ id: placeholders.email })} />
              </Form.Item>
            </Col>
          </Row>

          <Row>
            <Col span={16}>
              <Form.Item label={formatMessage({ id: fields.city })} name="city">
                <Input placeholder={formatMessage({ id: placeholders.city })} />
              </Form.Item>
            </Col>
          </Row>

          <Row>
            <Col span={16}>
              <Form.Item label={formatMessage({ id: fields.epuap })} name="epuap">
                <Input placeholder={formatMessage({ id: placeholders.epuap })} />
              </Form.Item>
            </Col>
          </Row>

          <Row>
            <Col span={16}>
              <Form.Item label={formatMessage({ id: fields.street })} name="street">
                <Input placeholder={formatMessage({ id: placeholders.street })} />
              </Form.Item>
            </Col>
          </Row>

          <Row>
            <Col span={16}>
              <Form.Item label={formatMessage({ id: fields.postalCode })} name="postalCode">
                <Input placeholder={formatMessage({ id: placeholders.postalCode })} />
              </Form.Item>
            </Col>
          </Row>

          <Row>
            <Col span={16}>
              <Form.Item label={formatMessage({ id: fields.houseNo })} name="houseNo">
                <Input placeholder={formatMessage({ id: placeholders.houseNo })} />
              </Form.Item>
            </Col>
          </Row>

          <Row>
            <Col span={16}>
              <Form.Item label={formatMessage({ id: fields.flatNo })} name="flatNo">
                <Input placeholder={formatMessage({ id: placeholders.flatNo })} />
              </Form.Item>
            </Col>
          </Row>

          <Row>
            <Col span={16}>
              <Form.Item label={formatMessage({ id: fields.nip })} name="nip">
                <Input placeholder={formatMessage({ id: placeholders.nip })} />
              </Form.Item>
            </Col>
          </Row>

          <Row>
            <Col span={16}>
              <Form.Item label={formatMessage({ id: fields.regon })} name="regon">
                <Input placeholder={formatMessage({ id: placeholders.regon })} />
              </Form.Item>
            </Col>
          </Row>

          <Row>
            <Col span={16}>
              <Form.Item label={formatMessage({ id: fields.comment })} name="comment">
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
              <Form.Item label={formatMessage({ id: fields.tags })} name="tags">
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
