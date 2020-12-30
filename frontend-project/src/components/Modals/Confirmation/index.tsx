import React, { useEffect, useState } from 'react';
import { Modal, Button } from 'antd';
import { localeKeys } from '@/locales/pl-PL';
import { formatMessage } from 'umi-plugin-react/locale';

type ConfirmationProps = {
  title?: string;
  onSuccess?: () => void;
  onFailure?: (error: Error) => void;
};

type ConfirmationModalProps = ConfirmationProps & {
  title: string;
  hideModal: () => void;
  onSubmit: () => void;
};

const ConfirmationModal = ({
  onSubmit,
  title,
  onSuccess,
  onFailure,
  hideModal,
}: ConfirmationModalProps) => {
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
        onFailure(error);
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
  props: ConfirmationProps,
  onSubmit: (args: T) => void,
) => {
  const [modal, setModal] = useState(null);

  const hideModal = () => setModal(null);

  const showModal = (args: T, title?: string) => {
    setModal(
      <ConfirmationModal
        {...props}
        {...(title ? { title } : undefined)}
        onSubmit={() => onSubmit(args)}
        hideModal={hideModal}
      />,
    );
  };

  return [modal, showModal];
};

export default ConfirmationModal;
