import React from "react";

class ErrorBoundary
extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  static getDerivedStateFromError() {
    return {
      hasError: true,
    };
  }

  componentDidCatch(error) {
    console.error(error);
  }

  render() {
    if (
      this.state.hasError
    ) {
      return (
        <div className="error-page">
          <h1>
            Something Went Wrong
          </h1>
        </div>
      );
    }

    return this.props.children;
  }
}

export default ErrorBoundary;