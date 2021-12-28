job "robot_Sangoma" {
  datacenters = ["dc1"]
  
  group "robots" {
    task "sangoma" {
      driver = "raw_exec"
      config {
 				command = "${NOMAD_TASK_DIR}\\repo\\rcc"
				args    = ["run","-e", "${NOMAD_TASK_DIR}\\local\\repo\\devdata\\env.json"]
      }
      artifact {
        source      = "https://github.com/arcontechnologies/RobotFramework.git"
        destination = "local\\repo"
      }
    }
  }
}

