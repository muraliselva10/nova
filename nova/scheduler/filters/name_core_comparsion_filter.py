import json

from oslo_log import log as logging
from nova.scheduler import filters

LOG = logging.getLogger(__name__)

class CustomFilter(filters.BaseHostFilter):

    def host_passes(self, host_state, spec_obj):
        instance_name = spec_obj.flavor.extra_specs['instance_name']
        cpu_info = host_state.cpu_info
        cpu_info = json.loads(cpu_info)
        cores = cpu_info["topology"]['cores']
        instance_name_length = len(instance_name)
        LOG.debug("Obtained core details {0}, Obtained instance name {1}, Obtained instance_name lenght {2}".format(cores, instance_name, instance_name_length))
        if instance_name_length <= int(cores):
            LOG.debug("Proceeding for VM provisioning on host {0} for VM {1}".format(host_state.host, instance_name))
            return True
        else:
            LOG.debug("Not Proceeding for VM provisioning on host {0} for VM {1}".format(host_state.host, instance_name))
            return False

