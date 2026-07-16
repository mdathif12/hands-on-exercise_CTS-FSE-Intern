# Hands-On 10

## State Management Comparison

React + Redux Toolkit
- Uses slices and createAsyncThunk.
- Moderate boilerplate.
- Excellent DevTools support.
- Very flexible.

Angular + NgRx
- Inspired by Redux.
- Uses Actions, Reducers, Effects, Selectors.
- Highest boilerplate.
- Best for large enterprise applications.

Vue + Pinia
- Simplest API.
- Minimal boilerplate.
- Built into Vue ecosystem.
- Easier learning curve.

NgRx Data Flow

Component
↓
Dispatch Action
↓
Effect
↓
API Call
↓
Reducer
↓
Store Update
↓
Selector
↓
Component