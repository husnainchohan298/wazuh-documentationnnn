# -- Redirects within the same release  -------------------------------------------------

# Important: the redirect is relative to the old path

redirectSameRelease = {
  '4.7': {
    '/cloud-service/cold-storage/index.html':
      '/cloud-service/archive-data/index.html',
    '/cloud-service/cold-storage/access.html':
      '/cloud-service/archive-data/access.html',
    '/cloud-service/cold-storage/configuration.html':
      '/cloud-service/archive-data/configuration.html',
    '/cloud-service/cold-storage/filename-format.html':
      '/cloud-service/archive-data/filename-format.html',
    '/cloud-service/getting-started/register-agents.html':
      '/cloud-service/getting-started/enroll-agents.html',
    '/user-manual/capabilities/osquery.html':
      '/user-manual/capabilities/malware-detection/osquery.html',
    '/user-manual/manager/manual-backup-restore.html':
      '/upgrade-guide/manual-backup-restore.html',
    '/user-manual/files-backup/index.html':
      '/migration-guide/files-backup/index.html',
    '/user-manual/files-backup/creating/index.html':
      '/migration-guide/files-backup/creating/index.html',
    '/user-manual/files-backup/creating/wazuh-agent.html':
      '/migration-guide/files-backup/creating/wazuh-agent.html',
    '/user-manual/files-backup/creating/wazuh-central-components.html':
      '/migration-guide/files-backup/creating/wazuh-central-components.html',
    '/user-manual/files-backup/restoring/index.html':
      '/migration-guide/files-backup/restoring/index.html',
    '/user-manual/files-backup/restoring/wazuh-agent.html':
      '/migration-guide/files-backup/restoring/wazuh-agent.html',
    '/user-manual/files-backup/restoring/wazuh-central-components.html':
      '/migration-guide/files-backup/restoring/wazuh-central-components.html',
    '/user-manual/agent-enrollment/via-agent-configuration/index.html':
      '/user-manual/agent/agent-enrollment/enrollment-methods/via-agent-configuration/index.html',
    '/user-manual/agent-enrollment/via-agent-configuration/linux-endpoint.html':
      '/user-manual/agent/agent-enrollment/enrollment-methods/via-agent-configuration/linux-endpoint.html',
    '/user-manual/agent-enrollment/via-agent-configuration/macos-endpoint.html':
      '/user-manual/agent/agent-enrollment/enrollment-methods/via-agent-configuration/macos-endpoint.html',
    '/user-manual/agent-enrollment/via-agent-configuration/windows-endpoint.html':
      '/user-manual/agent/agent-enrollment/enrollment-methods/via-agent-configuration/windows-endpoint.html',
    '/user-manual/agent-enrollment/via-manager-API/importing-the-key.html':
      '/user-manual/agent/agent-enrollment/enrollment-methods/via-manager-API/importing-the-key.html',
    '/user-manual/agent-enrollment/via-manager-API/index.html':
      '/user-manual/agent/agent-enrollment/enrollment-methods/via-manager-API/index.html',
    '/user-manual/agent-enrollment/via-manager-API/requesting-the-key.html':
      '/user-manual/agent/agent-enrollment/enrollment-methods/via-manager-API/requesting-the-key.html',
    '/user-manual/agent-enrollment/index.html':
      '/user-manual/agent/agent-enrollment/index.html',
    '/user-manual/agent-enrollment/security-options/agent-identity-verification.html':
      '/user-manual/agent/agent-enrollment/security-options/agent-identity-verification.html',
    '/user-manual/agent-enrollment/security-options/index.html':
      '/user-manual/agent/agent-enrollment/security-options/index.html',
    '/user-manual/agent-enrollment/security-options/manager-identity-verification.html':
      '/user-manual/agent/agent-enrollment/security-options/manager-identity-verification.html',
    '/user-manual/agent-enrollment/security-options/using-password-authentication.html':
      '/user-manual/agent/agent-enrollment/security-options/using-password-authentication.html',
    '/user-manual/agent-enrollment/troubleshooting.html':
      '/user-manual/agent/agent-enrollment/troubleshooting.html',
    '/user-manual/agents/agent-connection.html':
      '/user-manual/agent/agent-management/agent-connection.html',
    '/user-manual/agents/agent-life-cycle.html':
      '/user-manual/agent/agent-management/agent-life-cycle.html',
    '/user-manual/agents/antiflooding.html':
      '/user-manual/agent/agent-management/antiflooding.html',
    '/user-manual/agents/grouping-agents.html':
      '/user-manual/agent/agent-management/grouping-agents.html',
    '/user-manual/agents/index.html':
      '/user-manual/agent/agent-management/index.html',
    '/user-manual/agents/key-request.html':
      '/user-manual/agent/agent-management/key-request.html',
    '/user-manual/agents/labels.html':
      '/user-manual/agent/agent-management/labels.html',
    '/user-manual/agents/listing/index.html':
      '/user-manual/agent/agent-management/listing/index.html',
    '/user-manual/agents/listing/listing.html':
      '/user-manual/agent/agent-management/listing/listing.html',
    '/user-manual/agents/listing/using-command-line.html':
      '/user-manual/agent/agent-management/listing/using-command-line.html',
    '/user-manual/agents/listing/wazuh-dashboard.html':
      '/user-manual/agent/agent-management/listing/wazuh-dashboard.html',
    '/user-manual/agents/query-configuration.html':
      '/user-manual/agent/agent-management/query-configuration.html',
    '/user-manual/agents/remote-upgrading/agent-upgrade-module.html':
      '/user-manual/agent/agent-management/remote-upgrading/agent-upgrade-module.html',
    '/user-manual/agents/remote-upgrading/create-custom-wpk/create-wpk-key.html':
      '/user-manual/agent/agent-management/remote-upgrading/create-custom-wpk/create-wpk-key.html',
    '/user-manual/agents/remote-upgrading/create-custom-wpk/generate-wpk-package-manually.html':
      '/user-manual/agent/agent-management/remote-upgrading/create-custom-wpk/generate-wpk-package-manually.html',
    '/user-manual/agents/remote-upgrading/custom-repository.html':
      '/user-manual/agent/agent-management/remote-upgrading/custom-repository.html',
    '/user-manual/agents/remote-upgrading/index.html':
      '/user-manual/agent/agent-management/remote-upgrading/index.html',
    '/user-manual/agents/remote-upgrading/install-custom-wpk.html':
      '/user-manual/agent/agent-management/remote-upgrading/install-custom-wpk.html',
    '/user-manual/agent/agent-management/remote-upgrading/upgrading-agent.html':
      '/user-manual/agent/agent-management/remote-upgrading/upgrading-agent.html',
    '/user-manual/agents/remote-upgrading/wpk-list.html':
      '/user-manual/agent/agent-management/remote-upgrading/wpk-list.html',
    '/user-manual/agents/remove-agents/index.html':
      '/user-manual/agent/agent-management/remove-agents/index.html',
    '/user-manual/agents/remove-agents/remove.html':
      '/user-manual/agent/agent-management/remove-agents/remove.html',
    '/user-manual/agents/remove-agents/restful-api-remove.html':
      '/user-manual/agent/agent-management/remove-agents/restful-api-remove.html',
    '/user-manual/deployment-variables/deployment-variables-aix.html':
      '/user-manual/agent/deployment-variables/deployment-variables-aix.html',
    '/user-manual/deployment-variables/deployment-variables-linux.html':
      '/user-manual/agent/deployment-variables/deployment-variables-linux.html',
    '/user-manual/deployment-variables/deployment-variables-macos.html':
      '/user-manual/agent/deployment-variables/deployment-variables-macos.html',
    '/user-manual/deployment-variables/deployment-variables-windows.html':
      '/user-manual/agent/deployment-variables/deployment-variables-windows.html',
    '/user-manual/deployment-variables/deployment-variables.html':
      '/user-manual/agent/deployment-variables/deployment-variables.html',
    '/user-manual/api/examples.html':
      '/user-manual/api/getting-started.html#usage-in-scripts',
    '/user-manual/configuring-cluster/advanced-settings.html':
      '/user-manual/manager/configuring-cluster/advanced-settings.html',
    '/user-manual/configuring-cluster/basics.html':
      '/user-manual/manager/configuring-cluster/basics.html',
    '/user-manual/configuring-cluster/cluster-management.html':
      '/user-manual/manager/configuring-cluster/cluster-management.html',
    '/user-manual/configuring-cluster/index.html':
      '/user-manual/manager/configuring-cluster/index.html',
    '/user-manual/ruleset/dynamic-fields.html':
      '/user-manual/ruleset/decoders/dynamic-fields.html',
    '/user-manual/ruleset/json-decoder.html':
      '/user-manual/ruleset/decoders/json-decoder.html',
    '/user-manual/ruleset/ruleset-xml-syntax/sibling-decoders.html':
      '/user-manual/ruleset/decoders/sibling-decoders.html',
  },
  '4.6': {
    '/cloud-security/azure/activity-services/active-directory/index.html':
      '/cloud-security/azure/activity-services/entra/index.html',
    '/cloud-security/azure/activity-services/active-directory/graph.html':
      '/cloud-security/azure/activity-services/entra/graph.html',
    '/user-manual/user-administration/single-sign-on/administrator/azure-active-directory.html':
      '/user-manual/user-administration/single-sign-on/administrator/microsoft-entra-id.html',
    '/user-manual/user-administration/single-sign-on/read-only/azure-active-directory.html':
      '/user-manual/user-administration/single-sign-on/read-only/microsoft-entra-id.html',
  },
  '4.4': {
    '/nist/index.html':
      '/compliance/nist/index.html',
    '/nist/visualization-and-dashboard.html':
      '/compliance/nist/visualization-and-dashboard.html',
    '/nist/log-data-analysis.html':
      '/compliance/nist/log-data-analysis.html',
    '/nist/configuration-assessment.html':
      '/compliance/nist/configuration-assessment.html',
    '/nist/malware-detection.html':
      '/compliance/nist/malware-detection.html',
    '/nist/file-integrity-monitoring.html':
      '/compliance/nist/file-integrity-monitoring.html',
    '/nist/system-inventory.html':
      '/compliance/nist/system-inventory.html',
    '/nist/vulnerability-detection.html':
      '/compliance/nist/vulnerability-detection.html',
    '/nist/active-response.html':
      '/compliance/nist/active-response.html',
    '/nist/threat-intelligence.html':
      '/compliance/nist/threat-intelligence.html',
    '/user-manual/capabilities/wazuh-archives.html':
      '/user-manual/manager/wazuh-archives.html',
    '/amazon/services/supported-services/elastic-load-balancing/index.html':
      '/cloud-security/amazon/services/supported-services/elastic-load-balancing/index.html',
    '/amazon/services/supported-services/elastic-load-balancing/alb.html':
      '/cloud-security/amazon/services/supported-services/elastic-load-balancing/alb.html',
    '/amazon/services/supported-services/elastic-load-balancing/nlb.html':
      '/cloud-security/amazon/services/supported-services/elastic-load-balancing/nlb.html',
    '/amazon/services/supported-services/elastic-load-balancing/clb.html':
      '/cloud-security/amazon/services/supported-services/elastic-load-balancing/clb.html',
    '/azure/activity-services/prerequisites/dependencies.html':
      '/cloud-security/azure/activity-services/prerequisites/dependencies.html',
  },
  '4.3': {
   '/user-manual/wazuh-dashboard/single-sign-on/index.html':
     '/user-manual/user-administration/single-sign-on/index.html',
   '/user-manual/wazuh-dashboard/single-sign-on/okta.html':
     '/user-manual/user-administration/single-sign-on/administrator/okta.html',
   '/user-manual/wazuh-dashboard/single-sign-on/azure-active-directory.html':
     '/user-manual/user-administration/single-sign-on/administrator/azure-active-directory.html',
   '/user-manual/wazuh-dashboard/single-sign-on/pingone.html':
     '/user-manual/user-administration/single-sign-on/administrator/pingone.html',
   '/user-manual/wazuh-dashboard/single-sign-on/google.html':
     '/user-manual/user-administration/single-sign-on/administrator/google.html',
   '/user-manual/wazuh-dashboard/single-sign-on/jumpcloud.html':
     '/user-manual/user-administration/single-sign-on/administrator/jumpcloud.html',
   '/user-manual/wazuh-dashboard/single-sign-on/onelogin.html':
     '/user-manual/user-administration/single-sign-on/administrator/onelogin.html',
   '/user-manual/user-administration/single-sign-on/okta.html':
     '/user-manual/user-administration/single-sign-on/administrator/okta.html',
   '/user-manual/user-administration/single-sign-on/azure-active-directory.html':
     '/user-manual/user-administration/single-sign-on/administrator/azure-active-directory.html',
   '/user-manual/user-administration/single-sign-on/pingone.html':
     '/user-manual/user-administration/single-sign-on/administrator/pingone.html',
   '/user-manual/user-administration/single-sign-on/google.html':
     '/user-manual/user-administration/single-sign-on/administrator/google.html',
   '/user-manual/user-administration/single-sign-on/jumpcloud.html':
     '/user-manual/user-administration/single-sign-on/administrator/jumpcloud.html',
   '/user-manual/user-administration/single-sign-on/onelogin.html':
     '/user-manual/user-administration/single-sign-on/administrator/onelogin.html',
   '/user-manual/user-administration/single-sign-on/keycloak.html':
     '/user-manual/user-administration/single-sign-on/administrator/keycloak.html',
   '/user-manual/securing-wazuh/index.html':
     '/user-manual/user-administration/password-management.html',
   '/user-manual/securing-wazuh/wazuh-indexer.html':
     '/user-manual/user-administration/password-management.html',
   '/user-manual/securing-wazuh/opendistro.html':
     '/user-manual/user-administration/password-management.html',
   '/user-manual/securing-wazuh/elastic-stack.html':  
     '/user-manual/user-administration/password-management.html',
   '/user-manual/wazuh-dashboard/rbac.html':
     '/user-manual/user-administration/rbac.html', 
   '/learning-wazuh/build-lab/install-wazuh-central-components.html':
     '/proof-of-concept-guide/index.html',
  },
  '4.2': {
    '/release-notes/release_4_2_0.html':
      '/release-notes/release-4-2-0.html',
    '/user-manual/registering/agent-enrollment.html':  
      '/user-manual/agent-enrollment/via-agent-configuration/index.html',
    '/azure/dependencies.html':  
      '/azure/index.html',
  }
}
