# HiveBox – Progress Log

## Phase 1: Kickoff and Preparation

### Methodology
- Tracked work using a GitHub Projects Kanban board.
- Enforced a feature-branch workflow: all changes require Pull Requests, and direct pushes to main are blocked.

### Done
- Forked the HiveBox repository.
- Created a public Kanban board linked to the repository.
- Set up branch rulesets on main to require PRs and block force pushes or deletions

### senseBox IDs
- 5eba5fbad46fb8001b799786
- 5c21ff8f919bf8001adf2488
- 5ade1acf223bd80019a1011c

## Phase 2: Version function and Dockerfile

### Tools
- Installed Git, VS Code, Docker and Python

### Code 
- Implemented the code requirements in my GitHub repository forked for the project (done in phase 1) in project.py the function is print_version and the version v0.0.1

### Containers
- Created a Dockerfile for the project.
- Built the Docker image hivebox:v0.0.1 and ran it locally.

### Testing
**Prerequisites:** Docker installed and running.

**1. Build the image** (from the repository root):
```bash
docker build -t hivebox:v0.0.1 .
```

**2. Run the container:**
```bash
docker run hivebox:v0.0.1
```

**3. Expected output:**
```
v0.0.1
