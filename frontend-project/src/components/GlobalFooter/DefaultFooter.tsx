import React from 'react';
import { DefaultFooter as AntFooter } from '@ant-design/pro-layout';
import { GithubOutlined } from '@ant-design/icons';
import iconVercel from '../../assets/powered-by-vercel.svg';
import styles from './DefaultFooter.less';

const DefaultFooter = () => {
  return (
    <AntFooter
      copyright="2019-2020 Sieć Obywatelska Watchdog Polska"
      links={[
        {
          key: 'Sieć Obywatelska',
          title: 'Sieć Obywatelska Watchdog Polska',
          href: 'https://siecobywatelska.pl',
          blankTarget: true,
        },
        {
          key: `GitHub – Build time: ${BUILD_DATE}`,
          title: (
            <>
              small-eod – GitHub <GithubOutlined />
            </>
          ),
          href:
            typeof BUILD_SHA === 'undefined' || BUILD_SHA === 'unknown_sha'
              ? 'https://github.com/watchdogpolska/small_eod/'
              : `https://github.com/watchdogpolska/small_eod/commit/${BUILD_SHA}`,
          blankTarget: true,
        },
        {
          key: `Powered with vercel`,
          title: (
            <>
              <img className={styles.logo_vercel} alt="Powered with vercel" src={iconVercel} />
            </>
          ),
          href: 'http://vercel.com/?utm_source=watchdogpolska&utm_campaign=small_eod',
          blankTarget: true,
        },
        {
          key: 'redoc',
          title: 'small-eod – API ReDoc',
          href: '/api/redoc/',
          blankTarget: true,
        },
        {
          key: 'swagger',
          title: 'small-eod – API Swagger',
          href: '/api/docs/',
          blankTarget: true,
        },
        {
          key: 'drf',
          title: 'small-eod - API DRF',
          href: '/api/',
          blankTarget: true,
        },
      ]}
    />
  );
};

export default DefaultFooter;
