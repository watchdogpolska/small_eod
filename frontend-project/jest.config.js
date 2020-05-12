module.exports = {
  testURL: 'http://localhost:8000',
  preset: 'jest-puppeteer',
  extraSetupFiles: ['./tests/setupTests.ts'],
  globals: {
    ANT_DESIGN_PRO_ONLY_DO_NOT_USE_IN_YOUR_PRODUCTION: false,
    localStorage: null,
  },
  transform: {
    '^.+\\.ts?$': 'ts-jest',
  },
  testMatch: ['**/?(*.)+(spec|test).[t]s'],
};
