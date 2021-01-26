import { Link, formatMessage } from 'umi';
import { Result, Button } from 'antd';
import React, { ReactNode } from 'react';

export default (): ReactNode => (
  <Result
    status="404"
    title="404"
    style={{
      background: 'none',
    }}
    subTitle={formatMessage({
      id: 'exceptionand404.description.404',
      defaultMessage: 'Sorry, the page you visited does not exist.',
    })}
    extra={
      <Link to="/">
        <Button type="primary">
          {formatMessage({
            id: 'exceptionand404.exception.back',
            defaultMessage: 'Back Home',
          })}
        </Button>
      </Link>
    }
  />
);
