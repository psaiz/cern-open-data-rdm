# Quick Setup Guide for Testing

## 🚀 Installation Steps

### Step 1: Install Dependencies
```bash
# Install all testing dependencies
npm install
```

### Step 2: Run Tests
```bash
# Run all tests
npm test

# Or run the complete setup (install + test)
npm run setup
```

## 📦 Dependencies Installed

The following testing dependencies will be installed:

### Core Testing Framework
- `jest` - Testing framework
- `@testing-library/react` - React testing utilities
- `@testing-library/jest-dom` - DOM testing matchers
- `@testing-library/user-event` - User interaction simulation

### Build Tools
- `babel-jest` - JavaScript transformation
- `@babel/core`, `@babel/preset-env`, `@babel/preset-react` - ES6+/JSX support

### Test Environment
- `jest-environment-jsdom` - DOM environment for tests
- `identity-obj-proxy` - CSS module mocking
- `jest-transform-stub` - Asset file mocking

## 🔧 Alternative Minimal Setup

If you want to run tests without installing all dependencies, you can create a minimal test runner:

### Create minimal-test.js
```javascript
// Simple test runner for basic functionality testing
const assert = require('assert');

// Import your utility functions
const { toHumanReadableSize, isValidEmail } = require('./utils');

// Basic tests
console.log('Running minimal tests...');

// Test file size utility
try {
  assert.strictEqual(toHumanReadableSize(1024), '1.0 KiB');
  assert.strictEqual(toHumanReadableSize(0), '0 bytes');
  console.log('✅ File size utility tests passed');
} catch (e) {
  console.log('❌ File size utility tests failed:', e.message);
}

// Test email validation
try {
  assert.strictEqual(isValidEmail('test@example.com'), true);
  assert.strictEqual(isValidEmail('invalid-email'), false);
  console.log('✅ Email validation tests passed');
} catch (e) {
  console.log('❌ Email validation tests failed:', e.message);
}

console.log('Minimal tests completed!');
```

### Run minimal tests
```bash
node minimal-test.js
```

## 🏃‍♂️ Quick Test Commands

```bash
# Full installation and test
npm run setup

# Just install dependencies
npm install

# Run tests once
npm test

# Run tests in watch mode (for development)
npm run test:watch

# Run with coverage report
npm run test:coverage

# Run specific test file
npm test -- utils.test.js

# Run tests matching pattern
npm test -- --testNamePattern="should render"
```

## 🐛 Troubleshooting

### "jest: command not found"
**Solution**: Run `npm install` first, then use `npm test` (not `jest` directly)

### "Module not found" errors
**Solution**: Make sure all dependencies are installed:
```bash
rm -rf node_modules package-lock.json
npm install
```

### Permission errors
**Solution**: Use npx to run local binaries:
```bash
npx jest --version
```

### React/JSX transformation errors
**Solution**: Make sure Babel is configured correctly:
```bash
# Check if .babelrc.js exists
ls -la .babelrc.js

# Install babel dependencies if missing
npm install --save-dev @babel/core @babel/preset-env @babel/preset-react babel-jest
```

## 📍 Current Directory Check

Make sure you're in the correct directory:
```bash
pwd
# Should output: /path/to/cernopendata-portal/cernopendata/modules/theme/assets/semantic-ui/js/records

ls -la
# Should show: package.json, jest.config.js, __tests__/ directory, etc.
```

## 🔄 Node.js Version Requirements

- **Node.js**: >= 14.0.0
- **npm**: >= 6.0.0

Check your versions:
```bash
node --version
npm --version
```

If you need to update Node.js, use a version manager like nvm:
```bash
# Install/use Node.js 18
nvm install 18
nvm use 18
```

## 💡 Tips for Success

1. **Always run `npm install` first** before running tests
2. **Use `npm test`** instead of running `jest` directly
3. **Check the console output** for specific error messages
4. **Use `npm run test:debug`** if tests are failing mysteriously
5. **Run `npm run test:verbose`** for detailed test output

## 🆘 Still Having Issues?

If you continue to have problems:

1. **Clear everything and start fresh:**
   ```bash
   rm -rf node_modules package-lock.json
   npm install
   npm test
   ```

2. **Check if you have the required files:**
   ```bash
   ls -la __tests__/
   ls -la *.js
   cat package.json | grep jest
   ```

3. **Run the minimal test first** to verify basic functionality
4. **Check Node.js version compatibility**
