import { CheckCircleTwoTone } from '@ant-design/icons';
import React, { FC } from 'react';

export interface CheckIconProps {
  arg: boolean;
}

const CheckIcon: FC<CheckIconProps> = ({ arg }) =>
  arg ? (
    <CheckCircleTwoTone twoToneColor="#52C41A" />
  ) : (
    <CheckCircleTwoTone twoToneColor="#EB2F96" />
  );

export default CheckIcon;
