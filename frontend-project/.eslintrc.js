module.exports = {
  extends: [require.resolve('@umijs/fabric/dist/eslint')],
  globals: {
    page: true,
    BUILD_SHA: 'readonly',
    BUILD_BRANCH: 'readonly',
    BUILD_DATE: 'readonly',
  },
};
