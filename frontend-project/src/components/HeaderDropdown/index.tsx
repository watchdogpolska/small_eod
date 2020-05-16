import { DropDownProps } from 'antd/es/dropdown';
import { Dropdown } from 'antd';
import React, { ReactNode, FC } from 'react';
import classNames from 'classnames';
import styles from './index.less';

declare type OverlayFunc = () => ReactNode;

export interface HeaderDropdownProps extends Omit<DropDownProps, 'overlay'> {
  overlayClassName?: string;
  overlay: ReactNode | OverlayFunc | any;
  placement?: 'bottomLeft' | 'bottomRight' | 'topLeft' | 'topCenter' | 'topRight' | 'bottomCenter';
}

const HeaderDropdown: FC<HeaderDropdownProps> = ({ overlayClassName: cls, ...restProps }) => (
  <Dropdown overlayClassName={classNames(styles.container, cls)} {...restProps} />
);

export default HeaderDropdown;
