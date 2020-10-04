module.exports = {
  extends: [require.resolve('@umijs/fabric/dist/eslint')],
  globals: {
    page: true,
    build_sha: 'readonly',
    build_branch: 'readonly',
    build_date: 'readonly',
  },
};
