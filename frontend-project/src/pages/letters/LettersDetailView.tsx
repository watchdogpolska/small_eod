import { Uploader } from '@/components/Uploader/Uploader';
import { FileService } from '@/services/files';
import { PostData } from '@/services/service';
import { PageHeaderWrapper } from '@ant-design/pro-layout';
import { Button, Card, Col, DatePicker, Form, Input, Row, Select, Space, Spin, Switch } from 'antd';
import moment from 'moment';
import React, { useCallback, useEffect, useState } from 'react';
import { formatMessage, FormattedMessage } from 'umi-plugin-react/locale';
import router from 'umi/router';
import { FetchSelect } from '../../components/FetchSelect';
import { localeKeys } from '../../locales/pl-PL';
import { DetailMatchParam } from '../../models/connect';
import { AutocompleteService } from '../../services/autocomplete';
import { File as ResourceFile, Letter } from '../../services/definitions';
import { LettersService } from '../../services/letters';
import { getFormErrorFromPromiseError } from '../../utils/getFormErrorFromPromiseError';

const { TextArea } = Input;
const { Option } = Select;

const layout = {
  labelCol: { span: 8 },
  wrapperCol: { span: 16 },
};

const tailLayout = {
  wrapperCol: { offset: 8, span: 16 },
};

export default function LettersDetailView({ match }: DetailMatchParam) {
  const isEdit = Boolean(match.params.id);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [editedItem, setEditedItem] = useState<Letter | undefined>();
  const [form] = Form.useForm();
  const letterFileService = editedItem && FileService(editedItem);
  const {
    directions,
    fields,
    detailView: { editPageHeaderContent, newPageHeaderContent, placeholders, errors },
  } = localeKeys.letters;

  useEffect(() => {
    if (isEdit) LettersService.fetchOne(match.params.id).then(response => setEditedItem(response));
  }, []);

  function onError(response: any) {
    setIsSubmitting(false);
    if (response?.status === 400) {
      form.setFields(getFormErrorFromPromiseError(response));
    }
  }

  const submit = useCallback(
    async (edit: boolean = false) => {
      try {
        await form.validateFields();
      } catch {
        return;
      }
      const action = isEdit ? LettersService.update : LettersService.create;
      action({
        ...(form.getFieldsValue() as Letter),
        id: Number(match.params.id),
      })
        .then(letter =>
          edit ? router.push(`/letters/edit/${letter.id}`) : router.push('/letters'),
        )
        .catch(onError);
      setIsSubmitting(true);
    },
    [form],
  );

  function onAttachmentUpload(file: File): Promise<ResourceFile> {
    return letterFileService.uploadFile(file.name, file).then(path =>
      letterFileService.create({
        path,
        name: file.name,
      } as PostData<ResourceFile>),
    );
  }

  function onAttachmentRemove(fileId: ResourceFile['id']) {
    return letterFileService?.remove(fileId);
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
  if (isEdit)
    form.setFieldsValue({
      ...editedItem,
      date: moment(editedItem.date),
    });

  return (
    <Form {...layout} form={form}>
      <PageHeaderWrapper
        content={formatMessage({
          id: isEdit ? editPageHeaderContent : newPageHeaderContent,
        })}
      >
        <Card bordered={false}>
          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: fields.referenceNumber })}
                name="referenceNumber"
                rules={[
                  {
                    required: true,
                    message: formatMessage({ id: errors.referenceNumber }),
                  },
                ]}
              >
                <Input placeholder={formatMessage({ id: placeholders.referenceNumber })} />
              </Form.Item>
            </Col>
          </Row>

          <Row>
            <Col span={16}>
              <Form.Item
                label={formatMessage({ id: fields.final })}
                name="final"
                valuePropName="checked"
              >
                <Switch />
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
              <Form.Item label={formatMessage({ id: fields.direction })} name="direction">
                <Select placeholder={formatMessage({ id: placeholders.direction })}>
                  <Option value="IN">{formatMessage({ id: directions.in })}</Option>
                  <Option value="OUT">{formatMessage({ id: directions.out })}</Option>
                </Select>
              </Form.Item>
            </Col>
          </Row>

          <Row>
            <Col span={16}>
              <Form.Item label={formatMessage({ id: fields.date })} name="date">
                <DatePicker
                  showTime
                  placeholder={formatMessage({
                    id: placeholders.date,
                  })}
                  style={{
                    width: '100%',
                  }}
                />
              </Form.Item>
            </Col>
          </Row>

          <Row>
            <Col span={16}>
              <Form.Item label={formatMessage({ id: fields.documentType })} name="documentType">
                <FetchSelect
                  placeholder={formatMessage({
                    id: placeholders.documentType,
                  })}
                  mode={undefined}
                  autocompleteFunction={AutocompleteService.documentTypes}
                />
              </Form.Item>
            </Col>
          </Row>

          <Row>
            <Col span={16}>
              <Form.Item label={formatMessage({ id: fields.channel })} name="channel">
                <FetchSelect
                  placeholder={formatMessage({
                    id: placeholders.channel,
                  })}
                  mode={undefined}
                  autocompleteFunction={AutocompleteService.channels}
                />
              </Form.Item>
            </Col>
          </Row>

          <Row>
            <Col span={16}>
              <Form.Item label={formatMessage({ id: fields.case })} name="case">
                <FetchSelect
                  placeholder={formatMessage({
                    id: placeholders.case,
                  })}
                  mode={undefined}
                  autocompleteFunction={AutocompleteService.cases}
                />
              </Form.Item>
            </Col>
          </Row>

          <Row>
            <Col span={16}>
              <Form.Item label={formatMessage({ id: fields.institution })} name="institution">
                <FetchSelect
                  placeholder={formatMessage({
                    id: placeholders.institution,
                  })}
                  mode={undefined}
                  autocompleteFunction={AutocompleteService.institutions}
                />
              </Form.Item>
            </Col>
          </Row>

          {isEdit && (
            <Row>
              <Col span={16}>
                <Form.Item label={formatMessage({ id: fields.institution })}>
                  <Uploader
                    files={editedItem.attachments}
                    onUpload={onAttachmentUpload}
                    onRemove={onAttachmentRemove}
                  />
                </Form.Item>
              </Col>
            </Row>
          )}

          <Row>
            <Col span={16}>
              <Form.Item {...tailLayout}>
                {editedItem ? (
                  <Button type="primary" onClick={() => submit()} htmlType="button">
                    <FormattedMessage id={localeKeys.form.save} />
                  </Button>
                ) : (
                  <Space size="small" direction="horizontal">
                    <Button type="default" onClick={() => submit()} htmlType="button">
                      <FormattedMessage id={localeKeys.form.save} />
                    </Button>

                    <Button type="primary" onClick={() => submit(true)} htmlType="button">
                      <FormattedMessage id={localeKeys.form.saveAndEdit} />
                    </Button>
                  </Space>
                )}
              </Form.Item>
            </Col>
          </Row>
        </Card>
      </PageHeaderWrapper>
    </Form>
  );
}
