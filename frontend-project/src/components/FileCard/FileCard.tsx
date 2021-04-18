import { DeleteOutlined } from '@ant-design/icons';
import { Button, Spin } from 'antd';
import React, { useState } from 'react';
import { File } from '../../services/definitions';
import styles from './file-card.less';

export function FileCard(props: { file: File; onRemove: () => Promise<any> }) {
  const [isRemoving, setRemoving] = useState(false);
  return (
    <div className={styles.downloadCard}>
      <a href={props.file.downloadUrl} target="_blank" rel="noreferer noopener">
        {props.file.name}
      </a>
      {isRemoving ? (
        <Spin className={styles.downloadCardButton} />
      ) : (
        <Button
          shape="circle"
          icon={<DeleteOutlined />}
          onClick={() => {
            setRemoving(true);
            props.onRemove().catch(() => setRemoving(false));
          }}
          className={styles.downloadCardButton}
          danger
        />
      )}
    </div>
  );
}
