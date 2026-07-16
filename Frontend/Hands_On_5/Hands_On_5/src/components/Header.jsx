function Header({ siteName, enrolledCount }) {
  return (
    <header className="header">
      <h1>{siteName}</h1>

      <nav>
        <a href="#">Home</a>
        <a href="#">Courses</a>
        <a href="#">Profile</a>
      </nav>

      <p>Enrolled Courses: {enrolledCount}</p>
    </header>
  );
}

export default Header;