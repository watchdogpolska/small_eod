import 'antd/dist/antd.css';
import { File as ResourceFile } from '@/services/definitions';
import { InboxOutlined } from '@ant-design/icons';
import { RcCustomRequestOptions, UploadFile } from 'antd/es/upload/interface';
import Dragger from 'antd/lib/upload/Dragger';
import React, { useState } from 'react';

export function Uploader(props: {
  files?: ResourceFile[];
  onUpload: (request: File) => Promise<ResourceFile>;
  onRemove: (fileId: ResourceFile['id']) => Promise<any>;
}) {
  function transformFiles(files: ResourceFile[]): UploadFile<ResourceFile>[] {
    return files.map(file => ({
      size: 0,
      uid: String(file.id),
      name: file.name,
      url: file.downloadUrl,
      type: 'text',
    }));
  }

  const [files, setFiles] = useState<UploadFile<ResourceFile>[]>(transformFiles(props.files || []));

  function onRemove(removedFile: UploadFile<ResourceFile>) {
    const id = Number(removedFile.uid);
    function removeFileFromState() {
      setFiles(state => state.filter(file => file.uid !== removedFile.uid));
    }
    return Number.isNaN(id)
      ? removeFileFromState()
      : props.onRemove(id).then(() => removeFileFromState());
  }

  function onUpload(request: RcCustomRequestOptions) {
    props
      .onUpload(request.file)
      .then(file => {
        setFiles(state => [...state, ...transformFiles([file])]);
        request.onSuccess({}, request.file);
      })
      .catch(err => request.onError(err));
  }

  return (
    <Dragger multiple defaultFileList={files} onRemove={onRemove} customRequest={onUpload}>
      <p className="ant-upload-drag-icon">
        <InboxOutlined />
      </p>
      <p className="ant-upload-text">Click or drag file to this area to upload</p>
    </Dragger>
  );
}
