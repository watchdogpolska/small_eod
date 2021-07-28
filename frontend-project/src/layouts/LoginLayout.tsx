import { getMenuData, getPageTitle, MenuDataItem } from '@ant-design/pro-layout';
import DefaultFooter from '@/components/GlobalFooter/DefaultFooter';
import { Helmet } from 'react-helmet';
import { Link } from 'umi';
import React, { FC } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import { connect } from 'dva';
import SelectLang from '@/components/SelectLang';
import { ConnectState, Route } from '@/models/connect';
import logo from '../assets/logo.png';
import eodLogo from '../assets/watchdog_eod_logo.svg';
import styles from './LoginLayout.less';

export interface LoginLayoutProps {
  breadcrumbNameMap: {
    [path: string]: MenuDataItem;
  };
  route: Route;
  location: Location;
}

const LoginLayout: FC<LoginLayoutProps> = props => {
  const {
    route = {
      routes: [],
    },
  } = props;
  const { routes = [] } = route;
  const {
    children,
    location = {
      pathname: '',
    },
  } = props;
  const { breadcrumb } = getMenuData(routes);
  const title = getPageTitle({
    pathname: location.pathname,
    formatMessage,
    breadcrumb,
    ...props,
  });
  return (
    <>
      <Helmet>
        <title>{title}</title>
        <meta name="description" content={title} />
        <link rel="apple-touch-icon" sizes="180x180" href="/favicons/apple-touch-icon.png" />
        <link rel="icon" type="image/png" sizes="32x32" href="/favicons/favicon-32x32.png" />
        <link rel="icon" type="image/png" sizes="16x16" href="/favicons/favicon-16x16.png" />
        <link rel="manifest" href="/favicons/site.webmanifest" />
        <link rel="mask-icon" href="/favicons/safari-pinned-tab.svg" color="#5bbad5" />
        <meta name="msapplication-TileColor" content="#da532c" />
        <meta name="theme-color" content="#ffffff" />
      </Helmet>

      <div className={styles.container}>
        <div className={styles.lang}>
          <SelectLang />
        </div>
        <div className={styles.content}>
          <div className={styles.top}>
            <div className={styles.header}>
              <Link to="/" className={styles.headerLink}>
                <img alt="logo" className={styles.logo} src={logo} />
                <img
                  alt="logo aplikacji elektroniczny obieg dokumentów"
                  className={styles.eodLogo}
                  src={eodLogo}
                />
                <h1 className={styles.title}>Small EOD</h1>
              </Link>
            </div>
            <div className={styles.desc}>
              System elektronicznego obiegu dokumentów stowarzyszenia Sieć Obywatelska Watchdog
              Polska
            </div>
          </div>
          {children}
        </div>
        <DefaultFooter />
      </div>
    </>
  );
};

export default connect(({ settings }: ConnectState) => ({ ...settings }))(LoginLayout);
