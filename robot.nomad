job "job_robot" {
  #periodic {
  #  cron             = "0 9 * * 1-5"
  #  prohibit_overlap = true
  #}
  datacenters = ["dc1"]
  group "group_robot" {
    #count = 1
    // task "setup_task" {
    //   driver = "raw_exec"
    //   config {
 		// 		command = "xcopy"
		// 		args    = ["D:\\RobotFramework\\","${NOMAD_ALLOC_DIR}\\run_task\\","/E"]
    //   }
    //   lifecycle {
    //     hook    = "prestart"
    //     sidecar = false
    //   }
    // }
    task "run_robot" {
      driver = "raw_exec"
      config {
 				command = "local/rcc"
				args    = ["run","-e", "local/devdata/env.json"]
      }
      artifact {
        source      = "https://github.com/arcontechnologies/RobotFramework/archive/refs/heads/master.zip"
        mode        = "file"
        destination = "/local"
      }
    }
  }
}

