# event-management-service
Responsibilities: Handles all event-related actions like creation, editing, deletion, and viewing.


---
**Quey Command for Event Management Service**

CREATE DATABASE IF NOT EXISTS event_management_service;
```
**Use the event_management_service database**
USE event_management_service;

DROP TABLE IF EXISTS calendar_entries;
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS organizations;


**Table for organizations or clubs hosting the events**
CREATE TABLE IF NOT EXISTS organizations (
    org_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

**Table for events**
CREATE TABLE IF NOT EXISTS events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    org_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    event_date DATETIME NOT NULL,
    location VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (org_id) REFERENCES organizations(org_id) ON DELETE CASCADE
);

**Table for integrating calendar entries (optional)**
CREATE TABLE IF NOT EXISTS calendar_entries (
    entry_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT NOT NULL,
    calendar_date DATETIME NOT NULL,
    reminder_time DATETIME,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE
);

**Insert sample data for organizations**
INSERT INTO organizations (name, description) VALUES
('Columbia Intramural Sports', 'Recreational sports at Columbia.'),
('Columbia Daily Spectator', 'Student newspaper at Columbia.');

**Insert sample data for events**
INSERT INTO events (org_id, title, description, event_date, location) VALUES
(1, 'Columbia NSOP', 'New student orientation program to welcome students to Columbia.', '2024-09-01 10:00:00', 'Butler Lawns'),
(2, 'Columbia Club Fair Day', 'An exhibition showcasing clubs on campus.', '2024-09-05 09:00:00', 'Low Steps'),
(2, 'Columbia Career Fair', 'An exhibition for showcasing available job opportunities for Columbia students.', '2024-09-10 09:00:00', 'Lerner Hall');
```

---
