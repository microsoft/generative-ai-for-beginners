#!/usr/bin/env node
/**
 * Model Context Protocol (MCP) Educational Example with Roundtable - TypeScript
 * ==========================================================================
 *
 * This TypeScript example demonstrates how to use the Roundtable MCP Server
 * for educational purposes, building on the function calling concepts from
 * the main lesson.
 *
 * Prerequisites:
 * - npm install -g @roundtable/mcp-server (coming soon)
 * - OR: pip install roundtable-ai (current method)
 * - At least one supported AI assistant installed
 *
 * Learning Objectives:
 * - Understand how MCP extends function calling in TypeScript/JavaScript
 * - See unified AI assistant management in web development contexts
 * - Learn to build educational web applications with multiple AI tools
 * - Integrate MCP with modern JavaScript frameworks
 */

import { spawn, exec } from 'child_process';
import { promisify } from 'util';
import * as fs from 'fs/promises';
import * as path from 'path';

const execAsync = promisify(exec);

interface DemoQuestion {
    question: string;
    category: string;
    bestAI: string;
    webContext: string;
}

interface MCPConfig {
    mcpServers: {
        [key: string]: {
            command: string;
            env?: Record<string, string>;
            args?: string[];
        };
    };
}

class EducationalMCPDemoTS {
    private availableAssistants: string[] = [];
    private demoQuestions: DemoQuestion[] = [
        {
            question: "Explain what a REST API is and how to use it in JavaScript",
            category: "web-concepts",
            bestAI: "gemini",
            webContext: "Essential for frontend-backend communication"
        },
        {
            question: "Create a React component for a todo list",
            category: "frontend-coding",
            bestAI: "codex",
            webContext: "Clean, reusable component architecture"
        },
        {
            question: "Review this Express.js route for security issues",
            category: "backend-review",
            bestAI: "claude",
            webContext: "Security and best practices analysis"
        },
        {
            question: "Debug this async/await function step by step",
            category: "debugging",
            bestAI: "cursor",
            webContext: "Interactive debugging for async code"
        }
    ];

    async checkRoundtableInstallation(): Promise<boolean> {
        try {
            const { stdout, stderr } = await execAsync('roundtable-ai --help');
            return !stderr && stdout.includes('roundtable');
        } catch (error) {
            return false;
        }
    }

    async discoverAvailableAssistants(): Promise<string[]> {
        try {
            const { stdout } = await execAsync('roundtable-ai --check');

            const available: string[] = [];
            const assistants = ['claude', 'codex', 'gemini', 'cursor'];

            for (const assistant of assistants) {
                if (stdout.toLowerCase().includes(assistant) &&
                    (stdout.includes('✓') || stdout.includes('available'))) {
                    available.push(assistant);
                }
            }

            return [...new Set(available)]; // Remove duplicates
        } catch (error) {
            console.log('⚠️  Discovery timeout or error - this is normal for first run');
            return [];
        }
    }

    async demonstrateMCPConcepts(): Promise<void> {
        console.log('🎓 Model Context Protocol (MCP) Educational Demo - TypeScript Edition');
        console.log('='.repeat(70));

        // 1. Installation Check
        console.log('\n1️⃣ Checking Roundtable Installation...');
        const isInstalled = await this.checkRoundtableInstallation();

        if (!isInstalled) {
            console.log('❌ Roundtable not installed');
            console.log('📋 Install with: pip install roundtable-ai');
            console.log('📋 (npm package coming soon!)');
            return;
        }
        console.log('✅ Roundtable is installed!');

        // 2. Tool Discovery
        console.log('\n2️⃣ Discovering Available AI Assistants...');
        this.availableAssistants = await this.discoverAvailableAssistants();

        if (this.availableAssistants.length === 0) {
            console.log('⚠️  No AI assistants detected');
            console.log('📋 Install at least one: claude, codex, gemini, or cursor');
        } else {
            console.log(`✅ Found ${this.availableAssistants.length} assistants:`);
            this.availableAssistants.forEach(assistant => {
                console.log(`   • ${assistant}`);
            });
        }

        // 3. Web Development Use Cases
        console.log('\n3️⃣ Web Development Use Cases for MCP:');
        this.demonstrateWebDevelopmentScenarios();

        // 4. Framework Integration Examples
        console.log('\n4️⃣ Framework Integration Examples:');
        this.showFrameworkIntegrations();
    }

    demonstrateWebDevelopmentScenarios(): void {
        const scenarios = {
            "Full-Stack Learning": {
                description: "Use different AIs for frontend, backend, and deployment",
                example: "React (Cursor) → Express API (Codex) → Review (Claude) → Deploy (Gemini)"
            },
            "Code Review Workflow": {
                description: "Multi-perspective code review for web applications",
                example: "Security review (Claude), Performance (Codex), UX (Gemini), Debugging (Cursor)"
            },
            "Educational Tutorials": {
                description: "Create comprehensive web development tutorials",
                example: "Concept explanation (Gemini) → Code examples (Codex) → Best practices (Claude)"
            },
            "Real-time Development": {
                description: "Switch AIs during development based on current needs",
                example: "Stuck on CSS? → Cursor. Need API design? → Codex. Want explanation? → Gemini"
            }
        };

        Object.entries(scenarios).forEach(([scenario, details]) => {
            console.log(`\n📚 ${scenario}:`);
            console.log(`   • ${details.description}`);
            console.log(`   • Example: ${details.example}`);
        });
    }

    showFrameworkIntegrations(): void {
        console.log('\n🎯 JavaScript Framework Examples:');

        this.demoQuestions.forEach((demo, index) => {
            console.log(`\n🔧 Example ${index + 1}: ${demo.category}`);
            console.log(`   Question: ${demo.question}`);
            console.log(`   Best AI: ${demo.bestAI}`);
            console.log(`   Web Context: ${demo.webContext}`);
            console.log(`   Why: ${this.getAIStrengthForWeb(demo.bestAI)}`);
        });
    }

    getAIStrengthForWeb(aiName: string): string {
        const strengths = {
            "claude": "Excellent for security review, code quality, and web best practices",
            "codex": "Generates clean React/Node.js code with modern patterns",
            "gemini": "Great for explaining web concepts, API design, and architecture",
            "cursor": "Interactive debugging and step-by-step web development guidance"
        };
        return strengths[aiName as keyof typeof strengths] || "General purpose web development assistant";
    }

    async createWebDevelopmentMCPConfigs(): Promise<void> {
        console.log('\n📝 Web Development MCP Configurations:');
        console.log('='.repeat(45));

        const configs = {
            "Next.js Project": {
                filePath: ".cursor/mcp.json",
                config: {
                    mcpServers: {
                        "roundtable-ai": {
                            command: "roundtable-ai",
                            env: {
                                CLI_MCP_SUBAGENTS: "codex,claude,cursor,gemini",
                                CLI_MCP_WORKING_DIR: process.cwd()
                            }
                        }
                    }
                }
            },
            "VS Code Web Project": {
                filePath: ".vscode/settings.json",
                config: {
                    "mcp.servers": {
                        "roundtable-ai": {
                            command: "roundtable-ai",
                            env: {
                                CLI_MCP_SUBAGENTS: "codex,claude,cursor,gemini",
                                CLI_MCP_WORKING_DIR: "${workspaceFolder}"
                            }
                        }
                    }
                }
            },
            "Package.json Scripts": {
                filePath: "package.json",
                config: {
                    scripts: {
                        "ai:check": "roundtable-ai --check",
                        "ai:start": "roundtable-ai",
                        "ai:codex": "roundtable-ai --agents codex",
                        "ai:claude": "roundtable-ai --agents claude",
                        "ai:all": "roundtable-ai --agents codex,claude,cursor,gemini"
                    }
                }
            }
        };

        for (const [platform, details] of Object.entries(configs)) {
            console.log(`\n🔧 ${platform}:`);
            console.log(`   File: ${details.filePath}`);
            console.log(`   Configuration:`);
            console.log(JSON.stringify(details.config, null, 6));
        }
    }

    async generateWebProjectExample(): Promise<void> {
        console.log('\n🚀 Web Project Example Using Multiple AIs:');
        console.log('='.repeat(45));

        const projectFlow = [
            {
                phase: "Project Planning",
                ai: "gemini",
                task: "Research best practices for todo app architecture",
                code: `// Ask Gemini: "What's the best architecture for a React todo app with Node.js backend?"`
            },
            {
                phase: "Frontend Component",
                ai: "codex",
                task: "Generate clean React component code",
                code: `
// Generated by Codex
import React, { useState } from 'react';

interface Todo {
  id: string;
  text: string;
  completed: boolean;
}

const TodoList: React.FC = () => {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [inputText, setInputText] = useState('');

  const addTodo = () => {
    if (inputText.trim()) {
      const newTodo: Todo = {
        id: Date.now().toString(),
        text: inputText,
        completed: false
      };
      setTodos([...todos, newTodo]);
      setInputText('');
    }
  };

  return (
    <div className="todo-app">
      <input
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        onKeyPress={(e) => e.key === 'Enter' && addTodo()}
        placeholder="Add a new todo..."
      />
      <button onClick={addTodo}>Add Todo</button>
      <ul>
        {todos.map(todo => (
          <li key={todo.id} className={todo.completed ? 'completed' : ''}>
            {todo.text}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TodoList;`
            },
            {
                phase: "Code Review",
                ai: "claude",
                task: "Review for accessibility and best practices",
                code: `// Claude's suggestions:
// 1. Add ARIA labels for screen readers
// 2. Implement proper focus management
// 3. Add error handling for edge cases
// 4. Consider using useCallback for performance
// 5. Add TypeScript strict mode compliance`
            },
            {
                phase: "Debugging Session",
                ai: "cursor",
                task: "Interactive debugging and optimization",
                code: `// Cursor helps with:
// - Step-by-step debugging of useState issues
// - Interactive testing of component behavior
// - Real-time code suggestions during development
// - Performance optimization tips`
            }
        ];

        projectFlow.forEach((step, index) => {
            console.log(`\n${index + 1}. ${step.phase} (${step.ai.toUpperCase()}):`);
            console.log(`   Task: ${step.task}`);
            console.log(`   Implementation:`);
            console.log(step.code);
        });
    }

    provideWebDevelopmentNextSteps(): void {
        console.log('\n🚀 Next Steps for Web Developers:');
        console.log('='.repeat(40));

        const steps = [
            "Install Roundtable: pip install roundtable-ai",
            "Set up MCP in your preferred web IDE (VS Code, Cursor)",
            "Try the multi-AI workflow with a simple React component",
            "Experiment with different AIs for frontend vs backend tasks",
            "Build a full-stack project using multiple AI assistants",
            "Create educational content showing AI-assisted web development",
            "Contribute to web development MCP tools and examples"
        ];

        steps.forEach((step, index) => {
            console.log(`${index + 1}. ${step}`);
        });

        console.log('\n📚 Web Development AI Resources:');
        console.log('• React + AI: Learn how to integrate AI assistants in React projects');
        console.log('• Node.js + MCP: Backend development with multiple AI assistants');
        console.log('• Full-Stack AI Workflows: End-to-end project development');
        console.log('• MCP for Web Teams: Collaborative development with unified AI tools');

        console.log('\n🔗 Useful Links:');
        console.log('• Roundtable Documentation: https://github.com/askbudi/roundtable');
        console.log('• MCP Specification: https://modelcontextprotocol.io');
        console.log('• Microsoft Learn: https://learn.microsoft.com');
    }
}

async function main(): Promise<void> {
    const demo = new EducationalMCPDemoTS();

    console.log('🎓 Welcome to the MCP Educational Demo - TypeScript Edition!');
    console.log('This demo shows how Model Context Protocol extends function calling');
    console.log('for modern web development with JavaScript/TypeScript.\n');

    try {
        // Run the demonstration
        await demo.demonstrateMCPConcepts();
        await demo.createWebDevelopmentMCPConfigs();
        await demo.generateWebProjectExample();
        demo.provideWebDevelopmentNextSteps();

        console.log('\n' + '='.repeat(60));
        console.log('🎉 Demo Complete! Ready to start web development with MCP?');
        console.log('💡 Try running: roundtable-ai --check');
        console.log('🌐 Build your next web project with unified AI assistance!');
        console.log('='.repeat(60));

    } catch (error) {
        console.error('❌ Error running demo:', error);
        console.log('💡 Make sure Roundtable is installed: pip install roundtable-ai');
    }
}

// Run the demo if this file is executed directly
if (require.main === module) {
    main().catch(console.error);
}

export { EducationalMCPDemoTS };