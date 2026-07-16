import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { CourseCardComponent } from '../course-card/course-card';

@Component({
  selector: 'app-course-list',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    CourseCardComponent
  ],
  templateUrl: './course-list.html',
  styleUrl: './course-list.css'
})
export class CourseListComponent implements OnInit {

  loading = true;

  searchTerm = '';

  courses = [
    {
      name: 'Data Structures and Algorithms',
      code: 'CS301',
      credits: 4,
      grade: 'A'
    },
    {
      name: 'Database Management Systems',
      code: 'CS302',
      credits: 4,
      grade: 'A+'
    },
    {
      name: 'Computer Networks',
      code: 'CS303',
      credits: 3,
      grade: 'B+'
    },
    {
      name: 'Operating Systems',
      code: 'CS304',
      credits: 4,
      grade: 'A'
    },
    {
      name: 'Web Development',
      code: 'CS305',
      credits: 3,
      grade: 'O'
    },
    {
      name: 'Cloud Computing',
      code: 'CS306',
      credits: 3,
      grade: 'A+'
    }
  ];

  ngOnInit(): void {
    setTimeout(() => {
      this.loading = false;
    }, 1000);
  }

  get filteredCourses() {
    return this.courses.filter(course =>
      course.name
        .toLowerCase()
        .includes(this.searchTerm.toLowerCase())
    );
  }
}