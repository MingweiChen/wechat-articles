# Claude Code支持AGENTS.md：AI编程终于有共同说明书了！

> AI编程Agent互通的第一步，不是所有模型用同一个API，而是项目规则、边界和工作习惯能在不同Agent之间迁移。

## 先看事实

- AIWeekly 2026-09-19：Claude Code 2.1.277可在缺少CLAUDE.md时读取AGENTS.md，并提供配置控制。
- InfoWorld 2026-09-21新闻列表提到“Claude Code now also accepts instructions in OpenAI’s Agents.md format”。
- OpenAI生态此前推动AGENTS.md作为Agent读取项目说明、编码规范和安全边界的轻量文件格式。
- Step 3.5查重：过去一周写过多个编程Agent项目，但未写AGENTS.md跨工具标准化；与9月17的Context Mode/Worktrunk角度不同。

## 小文件可能比大模型更重要

AGENTS.md看起来只是仓库里的一个说明文件，但它解决的是AI编程最烦的问题：每换一个Agent，就要重新解释项目结构、测试命令、代码风格和禁区。Claude Code愿意兼容这个格式，说明工具之间开始承认共同工作规约。

## Agent真正需要的是上下文契约

模型能不能写代码是一层，能不能按这个仓库的规矩写是另一层。AGENTS.md把“怎么构建、怎么测试、哪些文件别碰、出了错先看哪里”固化下来，相当于给AI员工发了一本入职手册。

## 标准化会降低切换成本

如果OpenAI、Anthropic和更多本地Agent都能读同一份说明，开发团队就不必被某个工具的私有配置锁死。今天用Claude Code，明天用Codex或本地Agent，至少项目上下文可以迁移。

## 这也是安全边界的起点

Agent越能动代码，越需要明确边界。哪些命令不能跑、哪些凭据不能读、哪些目录不能改，写进项目说明比靠临场提醒更可靠。AGENTS.md的价值不只是方便，更是把安全和流程前置。

## 最后一句

Claude Code支持AGENTS.md不是一个普通兼容项，而是AI编程工具走向工业化的信号。真正成熟的Agent生态，需要共同的项目说明书。

---

*合规说明：本文为产业新闻与技术趋势分析，不涉及中国政治红线，不包含投资建议或个股推荐；公司、项目和产品仅作新闻事实与行业观察。*