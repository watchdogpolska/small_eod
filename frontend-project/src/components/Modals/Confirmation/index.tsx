import React, { useEffect, useState } from 'react';
import { Modal, Button } from 'antd';
import { localeKeys } from '@/locales/pl-PL';
import { formatMessage } from 'umi-plugin-react/locale';

type ConfirmationProps<T> = {
  title?: string;
  onSuccess?: () => void;
  onFailure?: (args: T) => void;
};

type ConfirmationModalProps<T> = ConfirmationProps<T> & {
  title: string;
  submitArgs: T;
  hideModal: () => void;
  onSubmit: () => void;
};

const ConfirmationModal = <T extends {}>({
  onSubmit,
  title,
  onSuccess,
  onFailure,
  hideModal,
  submitArgs,
}: ConfirmationModalProps<T>) => {
  const [isModalVisible, setIsModalVisible] = useState(true);
  const [isInProgress, setIsInProgress] = useState(false);

  useEffect(() => {
    if (!isModalVisible) {
      hideModal();
    }
  }, [isModalVisible]);

  const handleOk = async () => {
    setIsInProgress(true);
    try {
      await onSubmit();
      setIsModalVisible(false);
      onSuccess();
    } catch (error) {
      if (onFailure) {
        onFailure(submitArgs);
      }
    } finally {
      setIsInProgress(false);
    }
  };

  const handleCancel = () => {
    setIsModalVisible(false);
  };

  return (
    <>
      <Modal
        title={title}
        visible={isModalVisible}
        onOk={handleOk}
        onCancel={handleCancel}
        footer={[
          <Button key="confirmation-button-cancel" disabled={isInProgress} onClick={handleCancel}>
            {formatMessage({ id: localeKeys.modal.cancel })}
          </Button>,
          <Button
            key="confirmation-button-confirm"
            type="primary"
            disabled={isInProgress}
            loading={isInProgress}
            onClick={handleOk}
          >
            {formatMessage({ id: localeKeys.modal.confirm })}
          </Button>,
        ]}
      >
        <p>{formatMessage({ id: localeKeys.modal.description })}</p>
      </Modal>
    </>
  );
};

export const useConfirmationModal = <T extends {}>(
  props: ConfirmationProps<T>,
  onSubmit: (args: T) => void,
) => {
  const [modal, setModal] = useState(null);

  const hideModal = () => setModal(null);

  const showModal = (args: T, title?: string) => {
    setModal(
      <ConfirmationModal
        {...props}
        {...(title ? { title } : undefined)}
        submitArgs={args}
        onSubmit={() => onSubmit(args)}
        hideModal={hideModal}
      />,
    );
  };

  return [modal, showModal];
};

export default ConfirmationModal;
