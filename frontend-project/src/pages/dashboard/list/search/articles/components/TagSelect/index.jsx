import React, { Component } from 'react';
import { Tag } from 'antd';
import { UpOutlined, DownOutlined } from '@ant-design/icons';
import classNames from 'classnames';
import styles from './index.less';

const { CheckableTag } = Tag;

const TagSelectOption = ({ children, checked, onChange, value }) => (
  <CheckableTag
    checked={!!checked}
    key={value}
    onChange={state => onChange && onChange(value, state)}
  >
    {children}
  </CheckableTag>
);

TagSelectOption.isTagSelectOption = true;

class TagSelect extends Component {
  static defaultProps = {
    hideCheckAll: false,
    actionsText: {
      expandText: '展开',
      collapseText: '收起',
      selectAllText: '全部',
    },
  };

  static Option = TagSelectOption;

  static getDerivedStateFromProps(nextProps) {
    if ('value' in nextProps) {
      return {
        value: nextProps.value || [],
      };
    }

    return null;
  }

  constructor(props) {
    super(props);
    this.state = {
      expand: false,
      value: props.value || props.defaultValue || [],
    };
  }

  onChange = value => {
    const { onChange } = this.props;

    if (!('value' in this.props)) {
      this.setState({
        value,
      });
    }

    if (onChange) {
      onChange(value);
    }
  };

  onSelectAll = checked => {
    let checkedTags = [];

    if (checked) {
      checkedTags = this.getAllTags();
    }

    this.onChange(checkedTags);
  };

  getAllTags() {
    const { children } = this.props;
    const childrenArray = React.Children.toArray(children);
    const checkedTags = childrenArray
      .filter(child => this.isTagSelectOption(child))
      .map(child => child.props.value);
    return checkedTags || [];
  }

  handleTagChange = (value, checked) => {
    const { value: StateValue } = this.state;
    const checkedTags = [...StateValue];
    const index = checkedTags.indexOf(value);

    if (checked && index === -1) {
      checkedTags.push(value);
    } else if (!checked && index > -1) {
      checkedTags.splice(index, 1);
    }

    this.onChange(checkedTags);
  };

  handleExpand = () => {
    const { expand } = this.state;
    this.setState({
      expand: !expand,
    });
  };

  isTagSelectOption = node =>
    node &&
    node.type &&
    (node.type.isTagSelectOption || node.type.displayName === 'TagSelectOption');

  render() {
    const { value, expand } = this.state;
    const { children, hideCheckAll, className, style, expandable, actionsText = {} } = this.props;
    const checkedAll = this.getAllTags().length === value.length;
    const { expandText = '展开', collapseText = '收起', selectAllText = '全部' } = actionsText;
    const cls = classNames(styles.tagSelect, className, {
      [styles.hasExpandTag]: expandable,
      [styles.expanded]: expand,
    });
    return (
      <div className={cls} style={style}>
        {hideCheckAll ? null : (
          <CheckableTag checked={checkedAll} key="tag-select-__all__" onChange={this.onSelectAll}>
            {selectAllText}
          </CheckableTag>
        )}
        {value &&
          children &&
          React.Children.map(children, child => {
            if (this.isTagSelectOption(child)) {
              return React.cloneElement(child, {
                key: `tag-select-${child.props.value}`,
                value: child.props.value,
                checked: value.indexOf(child.props.value) > -1,
                onChange: this.handleTagChange,
              });
            }

            return child;
          })}
        {expandable && (
          <a className={styles.trigger} onClick={this.handleExpand}>
            {expand ? (
              <>
                {collapseText} <UpOutlined />
              </>
            ) : (
              <>
                {expandText}
                <DownOutlined />
              </>
            )}
          </a>
        )}
      </div>
    );
  }
}

export default TagSelect;
