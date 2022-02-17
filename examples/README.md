<!-- Copyright Yahoo. Licensed under the terms of the Apache 2.0 license. See LICENSE in the project root. -->

![Vespa logo](https://vespa.ai/assets/vespa-logo-color.png)

# Vespa Code examples


### [Vespa grouping and facets for organizing results ](part-purchases-demo)
A sample application demonstrating Vespa grouping and faceting for query time result analytics.
[Vespa grouping documentation](https://docs.vespa.ai/en/grouping.html)


### [Vespa predicate fields](boolean-search)
A sample app which demonstrates how to use Vespa's **predicate** field type to implement indexing of boolean expressions.
Boolean document side constraints allows the document to specify which type of queries it can be retrieved for.
This allows expressing logic like _"this document should only be visible in search for readers in age range 20 to 30"_
or "This product should only be visible in search during campaign hours".


## Self-hosted Deployments - operations
See [operations](operations) for sample applications for multinode clusters,
deployed in various infrastructure like Kubernetes.
Also find examples for security and monitoring .


### [Vespa custom linguistics Integration](vespa-chinese-linguistics)
This application demonstrates integrating custom linguistic processing,
in this case a Chinese tokenizer ([Jieba](https://github.com/fxsjy/jieba)).


### [Vespa custom HTTP api using request handlers and processors](http-api-using-request-handlers-and-processors)
This application demonstrates how to build custom HTTP apis,
building REST interfaces with custom handlers and renderers.
See also [Custom HTTP Api tutorial](https://docs.vespa.ai/en/jdisc/http-api-tutorial.html).


### [Vespa container plugins with multiple OSGI bundles](multiple-bundles)
This is a technical sample application demonstrating how to use multiple OSGI bundles for custom plugins
(searchers, handlers, renderers).


### joins
[joins](vespa-cloud/joins) shows possibilities for doing joins of data across nodes with
customer components. This is for use cases where parent-child is not sufficient,
and latency budgets are a bit higher.
<!-- ToDo: remove cloud specifics -->


### document-processing
[document-processing](vespa-cloud/document-processing) builds on album-recommendation to show
some of the possibilities for doing custom document processing in Java.
<!-- ToDo: remove cloud specifics -->


<!--
[generic-request-processing](generic-request-processing)
-->

----

Note: Applications with _pom.xml_ are Java/Maven projects and must be built before being deployed.
Refer to the [Developer Guide](https://docs.vespa.ai/en/developer-guide.html) for more information.

[Contribute](https://github.com/vespa-engine/vespa/blob/master/CONTRIBUTING.md) to the Vespa sample applications.

----

[![Vespa Sampleapps Search Feed](https://github.com/vespa-engine/sample-apps/actions/workflows/feed.yml/badge.svg)](https://github.com/vespa-engine/sample-apps/actions/workflows/feed.yml)

[![sample-apps link checker](https://cd.screwdriver.cd/pipelines/7038/link-checker-sample-apps/badge)](https://cd.screwdriver.cd/pipelines/7038/)

[![sample-apps build](https://cd.screwdriver.cd/pipelines/7038/build-apps/badge)](https://cd.screwdriver.cd/pipelines/7038/)

[![sample-apps verify-guides](https://cd.screwdriver.cd/pipelines/7038/verify-guides/badge)](https://cd.screwdriver.cd/pipelines/7038/)