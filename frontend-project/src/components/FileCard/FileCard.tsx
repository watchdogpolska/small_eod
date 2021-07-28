import { DeleteOutlined } from '@ant-design/icons';
import { Button, Spin } from 'antd';
import React, { useState } from 'react';
import { File } from '../../services/definitions';
import styles from './file-card.less';

export function FileCard(props: { file: File; onRemove: () => Promise<any> }) {
  const [isRemoving, setRemoving] = useState(false);
  function onRemove() {
    setRemoving(true);
    props.onRemove().catch(() => setRemoving(false));
  }

  return (
    <div className={styles.fileCard}>
      <a href={props.file.downloadUrl} target="_blank" rel="noopener noreferrer">
        {props.file.name}
      </a>
      {isRemoving ? (
        <Spin className={styles.downloadCardButton} />
      ) : (
        <Button
          shape="circle"
          icon={<DeleteOutlined />}
          onClick={onRemove}
          className={styles.fileCardButton}
          danger
        />
      )}
    </div>
  );
}
