job "job_Sangoma" {
  #periodic {
  #  cron             = "0 9 * * 1-5"
  #  prohibit_overlap = true
  #}
  datacenters = ["dc1"]
  group "group_tasks" {
    #count = 1
    task "setup_task" {
      driver = "raw_exec"
      config {
 				command = "xcopy"
				args    = ["D:\\RobotFramework\\","${NOMAD_ALLOC_DIR}\\run_task\\","/E"]
      }
      lifecycle {
        hook    = "prestart"
        sidecar = false
      }
    }
    task "run_task" {
      driver = "raw_exec"
      config {
 				command = "${NOMAD_ALLOC_DIR}\\run_task\\rcc"
				args    = ["run","-e", "${NOMAD_ALLOC_DIR}\\run_task\\devdata\\env.json"]
      }

    }
  }
}

