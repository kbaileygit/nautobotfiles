from nautobot.extras.jobs import Job
#from b import hello

class WillSucceed(Job):
    class Meta:
        description = 'test'
        commit_default = False

    def run(self, data, commit):
        return self.log_info(message=hello)
