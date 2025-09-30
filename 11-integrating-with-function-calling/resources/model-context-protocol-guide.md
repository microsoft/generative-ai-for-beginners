# Model Context Protocol (MCP) and Unified AI Assistant Management

[![Model Context Protocol Guide](../images/mcp-guide-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/genai-lesson11-mcp?WT.mc_id=academic-105485-koreyst)

## Introduction

Building on the function calling concepts from the main lesson, the **Model Context Protocol (MCP)** represents the next evolution in AI tool integration. While function calling allows individual LLMs to use external tools, MCP creates a standardized way for multiple AI assistants to work together seamlessly.

This guide will teach you:

- Understanding what MCP is and how it builds on function calling
- Setting up unified AI assistant management with Roundtable
- Creating educational projects that use multiple AI tools
- Building scalable AI workflows for learning and development

## Learning Goals

By the end of this guide, you will be able to:

- Explain how MCP extends function calling concepts
- Set up and configure multiple AI assistants through one interface
- Design educational workflows that leverage different AI capabilities
- Understand the benefits of unified AI tool management for learning

## What is the Model Context Protocol (MCP)?

The Model Context Protocol is an open standard that enables seamless integration between AI applications and external data sources and tools. Think of it as the "USB standard" for AI tools - just like USB allows any device to connect to any computer, MCP allows any AI assistant to connect to any tool or data source.

### Building on Function Calling

In the main lesson, you learned how function calling allows an LLM to:
1. **Identify** which external function to call
2. **Extract** the right parameters from user input
3. **Execute** the function and get results
4. **Present** results back to users in natural language

MCP takes this concept further by standardizing how **multiple** AI assistants can:
- Share the same tools and data sources
- Work together on complex tasks
- Maintain context across different AI services
- Provide unified interfaces for users

![MCP Architecture](../images/mcp-architecture.png?WT.mc_id=academic-105485-koreyst)

## Why MCP Matters for Education

### The Problem: AI Tool Fragmentation

As a student or educator, you might want to use different AI tools for different tasks:
- **Claude Code** for code review and debugging
- **GitHub Copilot** for code completion
- **Gemini** for research and explanations
- **Cursor** for interactive coding

But each tool requires different setup, authentication, and learning different interfaces.

### The Solution: Unified AI Assistant Management

MCP enables educational platforms to provide:
- **One Interface**: Access all AI tools through a single interface
- **Shared Context**: AI assistants share your project context and history
- **Easy Switching**: Compare different AI approaches to the same problem
- **Simplified Setup**: Install once, use everywhere

## Practical Example: Roundtable MCP Server

Let's explore this with a real-world educational tool: **Roundtable AI MCP Server**.

### What Roundtable Provides

Roundtable is an MCP server that unifies multiple AI coding assistants:

- **Automatic Discovery**: Finds installed AI tools on your system
- **Zero Configuration**: Works out of the box with detected tools
- **Unified Interface**: Same commands work with all AI assistants
- **Educational Focus**: Perfect for learning and comparing AI approaches

### Installation and Setup

```bash
# Install the unified AI assistant interface
pip install roundtable-ai

# Check which AI tools are available on your system
roundtable-ai --check

# Start the unified interface
roundtable-ai
```

### Integration with Popular Educational Tools

#### Claude Desktop (Perfect for AI Learning)
Add to your `~/.config/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "roundtable-ai": {
      "command": "roundtable-ai",
      "env": {
        "CLI_MCP_SUBAGENTS": "codex,claude,cursor,gemini",
        "CLI_MCP_WORKING_DIR": "/path/to/your/project"
      }
    }
  }
}
```

#### VS Code (Most Popular Student IDE)
Add to your `settings.json`:

```json
{
  "mcp.servers": {
    "roundtable-ai": {
      "command": "roundtable-ai",
      "env": {
        "CLI_MCP_SUBAGENTS": "codex,claude,cursor,gemini",
        "CLI_MCP_WORKING_DIR": "/path/to/your/project"
      }
    }
  }
}
```

#### Cursor (AI-First Learning Environment)
Create `.cursor/mcp.json` in your project:

```json
{
  "mcpServers": {
    "roundtable-ai": {
      "command": "roundtable-ai",
      "env": {
        "CLI_MCP_SUBAGENTS": "codex,claude,cursor,gemini"
      }
    }
  }
}
```

## Educational Use Cases

### 1. Comparative AI Learning

**Scenario**: Learning different approaches to code generation

```python
# Through MCP, students can ask the same question to different AI assistants
question = "Create a Python function to calculate fibonacci numbers"

# Each AI assistant provides different approaches:
# - Claude: Focuses on readability and explanation
# - Codex: Provides optimized, professional code
# - Gemini: Offers multiple implementation strategies
# - Cursor: Shows interactive development process
```

### 2. Multi-Step Learning Projects

**Scenario**: Building a complete web application

```python
# Step 1: Use Gemini for research and planning
research_prompt = "Explain the architecture for a simple todo app"

# Step 2: Use Codex for backend implementation
backend_prompt = "Create FastAPI backend for todo app"

# Step 3: Use Claude for code review and improvements
review_prompt = "Review this code for best practices and security"

# Step 4: Use Cursor for interactive frontend development
frontend_prompt = "Build React frontend with this API"
```

### 3. Code Review and Learning

**Scenario**: Understanding and improving code quality

```python
# Students can get multiple perspectives on the same code
code_review_questions = [
    "What are the potential bugs in this code?",          # Claude
    "How can this code be optimized?",                    # Codex
    "What design patterns could improve this?",           # Gemini
    "Show me step-by-step refactoring"                   # Cursor
]
```

## Building Your First MCP Educational Project

Let's create a simple educational project that demonstrates MCP concepts.

### Project: Multi-AI Code Learning Assistant

```python
# 1. Create a simple function calling setup (from main lesson)
def get_ai_assistance(question, ai_type="auto"):
    """
    Get assistance from different AI tools through MCP
    """
    if ai_type == "explanation":
        # Use Gemini for detailed explanations
        return f"Asking Gemini: {question}"
    elif ai_type == "code":
        # Use Codex for code generation
        return f"Asking Codex: {question}"
    elif ai_type == "review":
        # Use Claude for code review
        return f"Asking Claude: {question}"
    else:
        # Use Roundtable to automatically choose best AI
        return f"Asking Roundtable (auto-select): {question}"

# 2. Educational workflow
learning_questions = [
    ("What is a REST API?", "explanation"),
    ("Create a simple REST API in Python", "code"),
    ("Review this API code for best practices", "review"),
    ("Compare different implementation approaches", "auto")
]

for question, ai_type in learning_questions:
    response = get_ai_assistance(question, ai_type)
    print(f"Q: {question}")
    print(f"AI Response ({ai_type}): {response}")
    print("-" * 50)
```

### MCP Server Implementation

```python
# Example of how Roundtable implements MCP for education
class EducationalMCPServer:
    def __init__(self):
        self.available_assistants = self.discover_assistants()

    def discover_assistants(self):
        """Automatically find available AI tools"""
        assistants = {}

        # Check for common educational AI tools
        tools_to_check = ["claude", "codex", "gemini", "cursor"]

        for tool in tools_to_check:
            if self.is_tool_available(tool):
                assistants[tool] = self.create_tool_interface(tool)

        return assistants

    def route_educational_query(self, query, learning_objective):
        """Route queries to the best AI for educational purposes"""
        if "explain" in learning_objective.lower():
            return self.assistants.get("gemini", "default")
        elif "code" in learning_objective.lower():
            return self.assistants.get("codex", "default")
        elif "review" in learning_objective.lower():
            return self.assistants.get("claude", "default")
        else:
            return self.assistants.get("cursor", "default")
```

## Benefits for Educators and Students

### For Students
- **Easier Learning**: Compare different AI approaches to understand concepts better
- **Reduced Setup Time**: One installation gives access to multiple AI tools
- **Consistent Interface**: Focus on learning, not tool management
- **Better Understanding**: See how different AIs approach the same problem

### For Educators
- **Curriculum Flexibility**: Use the best AI tool for each learning objective
- **Simplified Classroom Setup**: One MCP server for entire class
- **Better Demonstrations**: Show multiple AI perspectives in real-time
- **Reduced Technical Barriers**: Students spend more time learning, less time configuring

### For Educational Institutions
- **Cost Effective**: Unified management reduces IT overhead
- **Scalable**: Easy to add new AI tools as they become available
- **Future-Proof**: Built on open standards that major companies support
- **Integration Ready**: Works with existing educational technology stacks

## Advanced Educational Scenarios

### 1. AI-Assisted Peer Programming

```python
# Students can pair program with multiple AI assistants
def ai_pair_programming_session(problem):
    roles = {
        "navigator": "claude",      # Explains approach and reviews
        "driver": "codex",          # Writes the actual code
        "researcher": "gemini",     # Looks up documentation
        "debugger": "cursor"        # Interactive problem solving
    }

    for role, ai_assistant in roles.items():
        print(f"{role.title()} ({ai_assistant}): Working on {problem}")
```

### 2. Multi-Language Learning

```python
# Compare how different AIs approach the same problem in different languages
def compare_language_implementations(algorithm):
    languages = ["python", "javascript", "java", "go"]
    ais = ["claude", "codex", "gemini"]

    for language in languages:
        for ai in ais:
            print(f"Implementing {algorithm} in {language} using {ai}")
            # Each AI provides different insights and approaches
```

### 3. Collaborative Project Development

```python
# Large educational projects with different AIs handling different aspects
def collaborative_project(project_type):
    phases = {
        "planning": "gemini",       # Research and architecture
        "backend": "codex",         # Core implementation
        "frontend": "cursor",       # Interactive development
        "testing": "claude",        # Quality assurance
        "documentation": "gemini"   # Clear explanations
    }

    for phase, ai in phases.items():
        print(f"Phase: {phase} - AI Assistant: {ai}")
```

## Getting Started: Your First MCP Educational Setup

### Step 1: Install Roundtable
```bash
pip install roundtable-ai
```

### Step 2: Check Available Tools
```bash
roundtable-ai --check
```

### Step 3: Configure Your Educational Environment
```bash
# For VS Code
echo '{
  "mcp.servers": {
    "roundtable-ai": {
      "command": "roundtable-ai",
      "env": {
        "CLI_MCP_SUBAGENTS": "codex,claude,cursor,gemini"
      }
    }
  }
}' >> ~/.vscode/settings.json
```

### Step 4: Start Learning!
```bash
# Launch your unified AI learning environment
roundtable-ai
```

## Troubleshooting Common Educational Setup Issues

### Issue: No AI Tools Detected
**Solution**: Install at least one supported AI tool first
```bash
# Install Claude Code (free)
pip install claude-cli

# Install Cursor (free with AI features)
# Download from cursor.sh

# Verify tools are working
roundtable-ai --check
```

### Issue: Configuration Not Working
**Solution**: Check file paths and permissions
```bash
# For VS Code
code ~/.vscode/settings.json

# For Claude Desktop
open ~/.config/claude_desktop_config.json
```

### Issue: Tools Not Responding
**Solution**: Verify API keys and authentication
```bash
# Check individual tools work first
claude --help
cursor --help

# Then test through Roundtable
roundtable-ai --agents claude,cursor
```

## Best Practices for Educational MCP Usage

### 1. Start Simple
- Begin with one or two AI assistants
- Focus on understanding MCP concepts before expanding
- Use familiar tools in your educational environment

### 2. Design for Learning Objectives
- Choose AI assistants based on educational goals
- Use Gemini for explanations and research
- Use Codex for clean, professional code examples
- Use Claude for code review and best practices
- Use Cursor for interactive learning

### 3. Encourage Comparison
- Have students ask the same question to different AIs
- Discuss why different AIs provide different approaches
- Use differences as teaching moments

### 4. Maintain Educational Focus
- Remember that MCP is a tool to enhance learning
- Don't let tool configuration distract from learning objectives
- Use unified interfaces to reduce cognitive load

## Next Steps in Your MCP Learning Journey

### Continue Learning
After mastering basic MCP concepts:

1. **Explore Advanced MCP Features**: Custom tool creation, data source integration
2. **Build Educational MCP Servers**: Create specialized tools for your curriculum
3. **Integrate with Educational Platforms**: Connect MCP to learning management systems
4. **Contribute to Educational MCP Tools**: Help improve tools like Roundtable

### Additional Resources
- [MCP Official Documentation](https://modelcontextprotocol.io?WT.mc_id=academic-105485-koreyst)
- [Roundtable AI GitHub Repository](https://github.com/askbudi/roundtable?WT.mc_id=academic-105485-koreyst)
- [Microsoft MCP for Beginners Course](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)

## Assignment: Build Your Own Educational MCP Workflow

Create an educational project that demonstrates MCP value:

### Option 1: Multi-AI Code Review System
- Set up Roundtable with 2-3 AI assistants
- Create a simple program with intentional issues
- Get code review feedback from each AI assistant
- Compare and contrast the different perspectives
- Document which AI provided the most helpful feedback for different types of issues

### Option 2: Collaborative Learning Project
- Choose a small programming project (calculator, todo app, etc.)
- Use different AI assistants for different project phases
- Document how each AI's strengths contributed to the project
- Create a presentation showing the collaborative development process

### Option 3: AI Teaching Assistant Comparison
- Prepare 5 programming questions at different difficulty levels
- Ask each question to different AI assistants through MCP
- Evaluate which AI provides the best educational value for each type of question
- Create guidelines for when to use which AI assistant for learning

## Great Work! Continue Your AI Education Journey

After completing this MCP guide, you have learned how to:
- Understand the relationship between function calling and MCP
- Set up unified AI assistant management for educational purposes
- Use multiple AI tools effectively for learning and development
- Build educational workflows that leverage different AI capabilities

Check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue leveling up your Generative AI knowledge!

---

*This guide was created to help educators and students understand how MCP builds on function calling concepts to create powerful, unified AI learning environments. For more educational AI resources, visit [Microsoft Learn](https://learn.microsoft.com?WT.mc_id=academic-105485-koreyst).*