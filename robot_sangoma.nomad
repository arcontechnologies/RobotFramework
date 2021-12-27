job "robot_Sangoma" {
  datacenters = ["dc1"]
  
  group "robots" {
    task "sangoma" {
      driver = "raw_exec"
      config {
 				command = "D:\\RobotFramework\\run_sangoma.bat"
				args    = [""]
      }
    }
  }
}

