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
 				command = "${NOMAD_TASK_DIR}\\repo\\rcc"
				args    = ["run","-e", "${NOMAD_TASK_DIR}\\repo\\devdata\\env.json"]
      }

    }
  }
}

